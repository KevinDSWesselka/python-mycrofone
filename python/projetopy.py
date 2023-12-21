import speech_recognition as sr

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

def gravar_audio():
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
                    print("Você disse: " + frase.strip())
                    return False
                if 'parar' in frase.lower():
                    print("Comando 'Parar' detectado. Gravação finalizada.")
                    frase = frase.replace('parar', '')
                    print("Você disse: " + frase.strip())
                    return True
                else:
                    print("Você disse: " + frase.replace('pausa', '').replace('parar', ''))
            except sr.UnknownValueError:
                print("Não entendi o que você disse!")
                frase = ""
            except sr.RequestError:
                print("Erro ao fazer a requisição para o serviço de reconhecimento de fala.")
            except KeyboardInterrupt:
                break

def reconhecer_fala():
    while True:
        acao = iniciar_gravacao()
        if acao == 'início':
            gravando = gravar_audio()
            if gravando:
                break
        elif acao == 'parar':
            break
        else:
            print("Comando inválido. Tente novamente.")

reconhecer_fala()
