# Polarita s.r.o. — AI agent workspace

Autonomní COO agent (Hermes) — monitoring, nabídky, správa.

## Struktura

```
monitoring/          # Skripty pro monitoring a operace
  check_email.py     # IMAP email monitoring (cron 15 min)
  make_offer.py      # Generátor nabídek z Schrack cart.csv
  gauth_url.py       # Google OAuth autorizační URL
  wp_create_pages.py # Vytvoření WP stránek přes REST API
  wp_update_home.py  # Aktualizace homepage

hermes/scripts/      # Skripty pro Hermes cron joby
  self_health.py     # Self-health check (gateway/telegram/cron/syncthing)
  check_email_hermes.py # Kopie check_email pro hermes scripts dir
```

## Přístupové údaje

**NEUKLÁDEJ DO GITU.** Použij `C:\Users\vacla\.secrets\polarita_credentials.txt`.

## Cron joby

| Job | Schedule | Co dělá |
|-----|----------|---------|
| Email monitoring | 15 min | Kontrola pošty → Telegram |
| Self-health | 10 min | Kontrola gateway/telegram/cron/syncthing |
| Denní briefing | 7:00 | Ranní souhrn → Telegram |
| ČSN licence | 8:00 | Kontrola aktivace licence |

## Web

- **polarita.cz** — WordPress (elektroinstalace, wallboxy)
- **polarita.eu** — Shoptet eshop
