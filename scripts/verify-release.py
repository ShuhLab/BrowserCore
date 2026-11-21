"""Public release consistency check: no credentials, account or browser session."""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib, io, json, zipfile

ROOT = Path(__file__).resolve().parents[1]
release = json.loads((ROOT / 'RELEASE.json').read_text())

def get(url, limit=4_000_000):
    request = Request(url, headers={'User-Agent': 'BrowserCore-Release-QA/1.0'})
    with urlopen(request, timeout=25) as response:
        data = response.read(limit + 1)
        if len(data) > limit:
            raise AssertionError('Response exceeds bound: ' + url)
        return data

public = json.loads(get('https://browser.m2g.pro/downloads/browser-core-release.json'))
assert public == release, 'Website and repository release metadata differ'
archives = {}
for entry in release['artifacts']:
    for base in ('https://browser.m2g.pro/downloads/', 'https://m2g.pro/browser-core/downloads/'):
        data = get(base + entry['filename'])
        assert len(data) == entry['size_bytes'], entry['filename']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['filename']
    archives[entry['filename']] = data
mac_name = next(name for name in archives if 'Mac-OneClick' in name)
ext_name = next(name for name in archives if 'Extension-' in name)
with zipfile.ZipFile(io.BytesIO(archives[mac_name])) as mac, zipfile.ZipFile(io.BytesIO(archives[ext_name])) as ext:
    for name in ext.namelist():
        if name.endswith('/'):
            continue
        basename = Path(name).name
        if not basename.endswith(('.js', '.html', '.json')):
            continue
        packaged = next(n for n in mac.namelist() if n.endswith('/agent/extension/' + basename))
        assert mac.read(packaged) == ext.read(name), 'Mac extension drift: ' + basename
    m = json.loads(ext.read(next(n for n in ext.namelist() if n.endswith('manifest.json'))))
    assert m['version'] == release['extension_version']
    # Chrome optional capabilities require a direct user gesture. They do not
    # grant background access, unlike an always-on host permission.
    assert set(m.get('optional_permissions', [])) == {'tabCapture', 'offscreen'}
    assert not m.get('host_permissions')
    assert not m.get('optional_host_permissions')
    assert set(m['permissions']) == {'activeTab', 'scripting', 'nativeMessaging', 'storage', 'alarms'}
for language in ('', 'ru/', 'de/', 'fr/', 'es/', 'pt/', 'zh/', 'ar/', 'hi/', 'tr/'):
    page = get('https://browser.m2g.pro/' + language).decode()
    assert '/downloads/' + mac_name in page, 'Old Mac link: ' + language
    assert '/downloads/' + ext_name in page, 'Missing extension link: ' + language
    assert 'id="current-release"' in page
linux = next(e for e in release['artifacts'] if 'Linux-BYO-' in e['filename'])
installer = get('https://browser.m2g.pro/downloads/install-linux.sh').decode()
assert linux['filename'] in installer and linux['sha256'] in installer
print('RELEASE_CONSISTENCY_PASSED: public hashes, two mirrors, bundled extension, 10 languages, Linux installer')
