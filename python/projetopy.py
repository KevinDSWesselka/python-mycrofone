#pinheirocfc@gmail.com
#Orientacoes em: https://youtu.be/vjXsa0I_dtc

#Essenciais
#pip install SpeechRecognition

#Extras
#pip install pipwin
#pipwin install pyaudio

import speech_recognition as sr
import csv

def iniciar_gravacao():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        while True:
            print("Diga 'início' ou 'parar'")
            audio = microfone.listen(source)
            try:
                frase = microfone.recognize_google(audio, language='pt-BR')
                return frase.lower()
            except sr.UnknownValueError:
                print("Não foi possível entender o comando. Tente novamente.")
            except sr.RequestError:
                print("Erro ao fazer a requisição para o serviço de reconhecimento de fala.")
            except KeyboardInterrupt:
                break

def gravar_audio(csv_writer):
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Comece a falar: ")
        while True:
            audio = microfone.listen(source)
            try:
                frase = microfone.recognize_google(audio, language='pt-BR')
                if 'pausa' in frase.lower():
                    print("Comando 'Pausa' detectado. Gravação pausada.")
                    frase = frase.replace('pausa', '')
                    print("Você disse: " + frase)
                    csv_writer.writerow(["Pausa", frase.strip()])
                    return False
                if 'parar' in frase.lower():
                    print("Comando 'Parar' detectado. Gravação finalizada.")
                    frase = frase.replace('parar', '')
                    print("Você disse: " + frase)
                    csv_writer.writerow(["Parar", frase.strip()])
                    return True
                else:
                    print("Você disse: " + frase)
                    csv_writer.writerow(["Ditado", frase.strip()])
            except sr.UnknownValueError:
                print("Não entendi o que você disse!")
                frase = ""
            except sr.RequestError:
                print("Erro ao fazer a requisição para o serviço de reconhecimento de fala.")
            except KeyboardInterrupt:
                break

def reconhecer_fala():
    with open('dados_gravacao.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Tipo", "Frase"])
        
        while True:
            acao = iniciar_gravacao()
            if acao == 'início':
                gravando = gravar_audio(csv_writer)
                if gravando:
                    break
            elif acao == 'parar':
                break
            else:
                print("Comando inválido. Tente novamente.")

reconhecer_fala()
