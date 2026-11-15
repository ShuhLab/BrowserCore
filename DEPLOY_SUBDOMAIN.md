# Activate browser.m2g.pro after DNS is confirmed

## Registrar step (REG.RU)

Create a DNS A record within m2g.pro:

- Subdomain: browser
- IPv4 address: 193.37.68.77
- Nameservers: ns1.reg.ru and ns2.reg.ru
- Do not change A/MX/TXT records for m2g.pro or any other project.

## Server-side activation (after A resolves)

1. Verify DNS publicly resolves to 193.37.68.77.
2. Use existing certbot/certbot container with current mounted
   /opt/nl-gateway/certbot/conf and /opt/nl-gateway/certbot/www volumes.
3. Obtain an ACME HTTP-01 certificate for browser.m2g.pro with webroot
   /var/www/certbot. Never request certificates before A exists.
4. Add the dedicated port-443 nginx virtual host pointing to
   /var/www/certbot/browser-m2g-pro, with exact allowed static routes:
   /, /docs, /support, /privacy, /terms and two ZIP downloads.
   All unknown routes should be 404, not proxy to another application.
5. Run nginx -t before reload.
6. Confirm HTTPS SAN, status 200, HSTS only after TLS works.
7. Do not move or overwrite https://m2g.pro/browser-core/mcp:
   owner OAuth redirect URLs and user connections depend on it.
8. Update public GitHub README with new product hostname once live.
