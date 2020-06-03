import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class Tone:
    def __init__(self, iama_authenticator, service_url):
        self.authenticator = IAMAuthenticator(iama_authenticator)
        self.tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            authenticator=self.authenticator
        )
        self.tone_analyzer.set_service_url(service_url)

    def get_tone(self, text):
        return self.tone_analyzer.tone(
            {'text': text},
            content_type='application/json'
        ).get_result()['document_tone']['tones']