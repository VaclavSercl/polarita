#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Google OAuth — maximalni VALIDNI scop (odstranen meetings.space)."""
import json
from urllib.parse import urlencode

CLIENT = json.load(open(r'C:\Users\vacla\.secrets\google_oauth_client.json'))['installed']
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar.events.owned',
    'https://www.googleapis.com/auth/contacts',
    'https://mail.google.com/',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/forms',
    'https://www.googleapis.com/auth/tasks',
    'https://www.googleapis.com/auth/meetings.space.readonly',
    'https://www.googleapis.com/auth/script.external_request',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtubepartner',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/photoslibrary',
    'https://www.googleapis.com/auth/analytics',
    'https://www.googleapis.com/auth/analytics.edit',
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/generative-language.retriever',
]

params = {
    'client_id': CLIENT['client_id'],
    'redirect_uri': 'urn:ietf:wg:oauth:2.0:oob',
    'response_type': 'code',
    'scope': ' '.join(SCOPES),
    'access_type': 'offline',
    'prompt': 'consent',
}
print('https://accounts.google.com/o/oauth2/v2/auth?' + urlencode(params))
