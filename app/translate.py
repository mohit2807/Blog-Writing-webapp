import requests
from flask_babel import _
from app import current_app

def translate(text,source_language,dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error')
    auth={
        'Ocp-Apim-Subscription-Key':current_app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'centralindia',
    }
    req=requests.post(
        'https://api.cognitive.microsofttranslator.com'
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language), headers=auth, json=[{'Text': text}])
    if req.status_code!=200:
        return _("error in service")
    return req.json()[0]['translations'][0]['text']