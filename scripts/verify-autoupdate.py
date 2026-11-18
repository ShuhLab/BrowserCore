"""Verify signed auto-update metadata against the release document."""
import json,urllib.request,time
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from pathlib import Path
r=json.loads(Path("RELEASE.json").read_text())
details=r["autoupdate"]
request=lambda url:urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"BrowserCore-Release-QA"}),timeout=15).read(20000)
raw=request(details["manifest_url"])
signature=request(details["signature_url"])
assert len(signature)==64
Ed25519PublicKey.from_public_bytes(bytes.fromhex(details["ed25519_public_key_hex"])).verify(signature,raw)
m=json.loads(raw)
assert m["schema"]==1 and m["product"]=="BrowserCore" and m["channel"]=="beta"
assert m["release_id"]==r["agent_version"]
assert m["published_at"]<=time.time()+300<m["expires_at"]
for platform,prefix in [("macos","Mac-OneClick"),("linux","Linux-BYO")]:
 entry=m["packages"][platform]
 src=next(x for x in r["artifacts"] if prefix in x["filename"])
 assert entry["filename"]==src["filename"] and entry["sha256"]==src["sha256"] and entry["bytes"]==src["size_bytes"]
print("SIGNED_UPDATE_MANIFEST_PASSED",m["release_id"])
