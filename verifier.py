import os
import requests


def verifier(page, response):
    secret = os.environ.get(page + '_GOOGLE_RECAPTCHA_SECRET')
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={'secret': secret, 'response': response})
    result = r.json()

    return result
