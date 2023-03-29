
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv




#translate english string to french string
def english_fo_french(english_text):
    
    load_dotenv()

    apikey = os.environ['apikey']
    url = os.environ['url']
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    translation = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()
    #print(translation['translations'][0]['translation'])
    french_text=translation['translations'][0]['translation']
    return french_text
#translate french string to enlglish string
def french_to_english(french_text):
    load_dotenv()

    apikey = os.environ['apikey']
    url = os.environ['url']
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    translation = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()
    #print(translation['translations'][0]['translation'])
    english_text=translation['translations'][0]['translation']
    return english_text

#print(englishToFrench('hi, how are you'))
#print(frenchToEnglish('Salut, comment tu es'))
#print(englishToFrench('hello'))