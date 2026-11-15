# browser.m2g.pro deployment record

DNS: A browser.m2g.pro -> 193.37.68.77 at REG.RU (verified 15 November 2026).
TLS: Let's Encrypt browser.m2g.pro certificate issued 15 November 2026, expires 13 February 2027.
Hosting: dedicated read-only Nginx virtual host /opt/nl-gateway/default.conf, static content under /opt/nl-gateway/certbot/www/browser-m2g-pro.
HTTPS routes: /, /docs, /support, /privacy, /terms, /sitemap.xml, /robots.txt, /downloads/* exact filenames.

The MCP endpoint and OAuth remain on https://m2g.pro/browser-core/mcp; do not move them without an explicit authorization migration.
Renewal: existing renew_gateway_certificates.sh invokes certbot renew for registered certificates.
No checkout or paid subscriptions currently enabled.
