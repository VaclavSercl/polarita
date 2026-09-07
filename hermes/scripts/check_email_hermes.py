#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Monitoring firemní pošty Polarita — nové zprávy → výstup pro agenta.
Běží jako cron job: spočítá nové zprávy od posledního běhu a vypíše je.
Stav si drží v D:\\Mourek\\Wendy\\AI\\Polarita\\monitoring\\email_state.json
"""
import imaplib, email, json, os, sys
from email.header import decode_header
from datetime import datetime, timezone

HOST = 'imap.forpsi.com'
USER = 'vaclav.sercl@polarita.cz'
STATE_FILE = r'D:\Mourek\Wendy\AI\Polarita\monitoring\email_state.json'
SECRETS = r'C:\Users\vacla\.secrets\polarita_credentials.txt'

def get_password():
    with open(SECRETS, encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('password_vaclav'):
                return line.split('=',1)[1].strip()
    return None

def dec(s):
    if not s: return ''
    return ''.join(p.decode(c or 'utf-8', errors='replace') if isinstance(p, bytes) else str(p)
                   for p, c in decode_header(s))

# PRIORITY odesílatelů — co vyžaduje okamžitou pozornost
PRIORITY_DOMAINS = ['uol.cz', 'bspi.cz', 'reporyje.cz']
PRIORITY_KEYWORDS = ['poptávka', 'poptavka', 'revize', 'objednávka', 'objednavka', 'faktura', 'nespárovan']

# SPAM / hromadný marketing — nehlásit (state/UID se přesto posune, takže se zpráva už nikdy nevrátí)
SPAM_DOMAINS = ['temuemail.com', 'solarvolt.com', 'mk-solar.com', 'photoktm.com', 'coingecko.com', 'pi-logistik.com', 'banggood.com', 'blink-9z.com']

def main():
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    state = {}
    if os.path.exists(STATE_FILE):
        state = json.load(open(STATE_FILE, encoding='utf-8'))
    last_uid = state.get('last_uid', 0)

    pw = get_password()
    if not pw:
        print('CHYBA: heslo nenalezeno v trezoru'); sys.exit(1)

    M = imaplib.IMAP4_SSL(HOST, 993, timeout=20)
    M.login(USER, pw)
    M.select('INBOX', readonly=True)

    # hledáme zprávy s UID větším než poslední viděné
    typ, data = M.uid('SEARCH', None, f'UID {last_uid+1}:*' if last_uid else 'ALL')
    uids = [int(u) for u in data[0].split()]
    uids = [u for u in uids if u > last_uid]

    if not uids:
        print('NO_NEW_MESSAGES')
        M.logout(); return

    lines = []
    new_max = last_uid
    for uid in uids[:30]:  # bezpečnostní strop na běh
        typ, d = M.uid('FETCH', str(uid), '(BODY[HEADER.FIELDS (FROM SUBJECT DATE)])')
        if not d or not d[0]:
            continue
        h = email.message_from_bytes(d[0][1])
        frm = dec(h.get('From', '')); subj = dec(h.get('Subject', ''))
        date = h.get('Date', '')[:20]
        new_max = max(new_max, uid)  # posunout state vždy (i pro přeskočený spam)
        if '*****spam*****' in subj.lower() or any(dom in frm.lower() for dom in SPAM_DOMAINS):
            continue  # server-spam marker (Forpsi) / hromadný marketing — potichu přeskočit
        urgent = any(dom in frm.lower() for dom in PRIORITY_DOMAINS) or \
                 any(k in subj.lower() for k in PRIORITY_KEYWORDS)
        flag = '🔴' if urgent else '⚪'
        lines.append(f'{flag} {date} | {subj[:70]} | {frm[:45]}')

    json.dump({'last_uid': new_max, 'updated': datetime.now(timezone.utc).isoformat()},
              open(STATE_FILE, 'w', encoding='utf-8'))
    M.logout()

    if lines:
        print(f'NOVÉ ZPRÁVY ({len(lines)}):')
        print('\n'.join(lines))
    else:
        print('NO_NEW_MESSAGES')

if __name__ == '__main__':
    main()
