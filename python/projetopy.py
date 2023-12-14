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
        print("Diga algo para iniciar a gravação: ")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            if 'início' in frase:  # Verifica se a palavra-chave 'Inicio' está na frase
                print("Comando 'Início' detectado. Iniciando a gravação.")
                return True
            else:
                print("Comando não reconhecido. Tente novamente.")
                return False
        except sr.UnknownValueError:
            print("Não foi possível entender o comando. Tente novamente.")
            return False

def reconhecer_fala():
    if iniciar_gravacao():
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Comece a falar: ")
            audio = microfone.listen(source)
            try:
                frase = microfone.recognize_google(audio, language='pt-BR')
                print("Você disse: " + frase)
            except sr.UnknownValueError:
                print("Não entendi o que você disse!")
                frase = ""
            return frase
    else:
        return ""

reconhecer_fala()
