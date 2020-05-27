import requests
from gtts import gTTS
from googletrans import Translator

def processarReconhecimentoDeImagem():
    subscription_key = "c48841d4c5b24f93aa4335d0fce18eb2"
    endpoint = "https://brazilsouth.api.cognitive.microsoft.com/"
    analyze_url = endpoint + "vision/v2.1/analyze"

    # caminho da imagem
    image_path = "C:/Users/Amplix/Desktop/Nova pasta/image4.jpg"

    # Leia a imagem em uma matriz de bytes
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    analysis = response.json()
    return analysis["description"]["captions"][0]["text"]

def traduzirTexto(description) :
    translator = Translator()
    descriptionPt = translator.translate(description, dest='pt').text
    return descriptionPt

def salvarAudios(descriptionEN,descriptionPT):
    tts = gTTS(descriptionEN)
    tts.save('audioEN.mp3')

    tts = gTTS(descriptionPT,lang='pt')
    tts.save('audioPT.mp3')


description = processarReconhecimentoDeImagem()
descriptionPt = traduzirTexto(description)
salvarAudios(description,descriptionPt)

print("Inglês: ", description)
print("Português: ", descriptionPt)
print("--------------------------")
print("Pressione Enter para sair ...")
input() 
