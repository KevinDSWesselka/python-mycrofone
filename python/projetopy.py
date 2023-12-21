#pinheirocfc@gmail.com
#Orientacoes em: https://youtu.be/vjXsa0I_dtc

#Essenciais
#pip install SpeechRecognition

#Extras
#pip install pipwin
#pipwin install pyaudio

import speech_recognition as sr

def iniciar_gravacao():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga 'início', 'pausa' ou 'parar'")
        while True:
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

def reconhecer_fala():
    gravando = False
    while True:
        acao = iniciar_gravacao()
        if acao == 'início':
            gravando = True
            microfone = sr.Recognizer()
            with sr.Microphone() as source:
                microfone.adjust_for_ambient_noise(source)
                print("Comece a falar: ")
                while gravando:
                    audio = microfone.listen(source)
                    try:
                        frase = microfone.recognize_google(audio, language='pt-BR')
                        print("Você disse: " + frase)
                        if 'pausa' in frase.lower():
                            print("Comando 'Pausa' detectado. Gravação pausada.")
                            gravando = False
                        if 'parar' in frase.lower():
                            print("Comando 'Parar' detectado. Gravação finalizada.")
                            return  # Encerra a função reconhecer_fala() e o programa
                    except sr.UnknownValueError:
                        print("Não entendi o que você disse!")
                        frase = ""
                    except sr.RequestError:
                        print("Erro ao fazer a requisição para o serviço de reconhecimento de fala.")
                    except KeyboardInterrupt:
                        gravando = False
                        break
        elif acao == 'parar':
            return  # Encerra o programa se 'parar' for detectado
        else:
            print("Comando inválido. Tente novamente.")

reconhecer_fala()