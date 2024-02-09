import speech_recognition as sr
from simple_salesforce import Salesforce
import datetime

# Credenciais de acesso ao Salesforce
username = 'ricardo.vicente.pc@resourceful-narwhal-w7e7wa.com'
password = 'rick.011'
security_token = 'DutB707Q9FjjxH5GSED2w4zM'

# Autenticação no Salesforce
sf = Salesforce(username=username, password=password, security_token=security_token)

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

def gravar_audio(lista_apontamentos):
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
                    return False
                if 'parar' in frase.lower():
                    print("Comando 'Parar' detectado. Gravação finalizada.")
                    frase = frase.replace('parar', '')
                    print("Você disse: " + frase)
                    return True
                else:
                    print("Você disse: " + frase)
                    # Create dictionary for the Salesforce object
                    novo_apontamento = {
                        'Name__c': 'Gravação de Áudio',
                        'Data_Inicio__c': datetime.datetime.now().strftime("%Y-%m-%d"),
                        'Descricao__c': frase,
                        'DuracaoHoras__c': '0',  # You might want to calculate the duration
                        # Add other fields as needed
                    }
                    lista_apontamentos.append(novo_apontamento)
            except sr.UnknownValueError:
                print("Não entendi o que você disse!")
                frase = ""
            except sr.RequestError:
                print("Erro ao fazer a requisição para o serviço de reconhecimento de fala.")
            except KeyboardInterrupt:
                break

def reconhecer_fala():
    lista_apontamentos = []
    while True:
        acao = iniciar_gravacao()
        if acao == 'início':
            gravando = gravar_audio(lista_apontamentos)
            if not gravando:
                break
        elif acao == 'parar':
            break
        else:
            print("Comando inválido. Tente novamente.")

    # Criação dos apontamentos no Salesforce
    try:
        for apontamento in lista_apontamentos:
            novo_apontamento = sf.Apontamento__c.create(apontamento)
            print("Novo apontamento criado:", novo_apontamento)
    except Exception as e:
        print("Erro ao criar apontamento:", e)

# Chame a função reconhecer_fala() para iniciar o reconhecimento de fala e a criação dos apontamentos no Salesforce
reconhecer_fala()
