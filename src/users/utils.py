import requests
from django.conf import settings


def fetch_google_user_info(token):
    headers = {'Authorization': f'Beaers {token}'}
    res = requests.get(url=settings.GOOGLE_USER_INFO_URL, headers=headers)
    if res.status_code == 200:
        return res.json()
    return None
