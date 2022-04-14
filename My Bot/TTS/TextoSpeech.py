from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def texttospeech():
    apikey = 'oYBbIBHteGbBjsqMuZua7g7Wsc3OXYJmqjaWf03PfVi9'
    url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/034ecad2-85b8-48a0-9d75-58e1833507a9'
# Setup Service
    authenticator = IAMAuthenticator(apikey)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)



    with open('C:\\Users\\StevenLi\\Desktop\\My Bot\\Chatbot\\readme.txt', 'r') as f:
        text = f.readlines()
    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)
    with open('./response.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3', voice='en-US_LisaV3Voice').get_result()
        audio_file.write(res.content)

texttospeech()