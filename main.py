import speech_recognition as sr
import pyttsx3

from importacoes import *

# Inicializando o sintetizador de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala

# Reconhecedor de voz
recognizer = sr.Recognizer()

# Agenda de tarefas
agenda = []

def speak(text):
    """Função para falar uma mensagem"""
    engine.say(text)
    engine.runAndWait()

def ouvir_comando():
    """Função para ouvir e reconhecer comandos de voz"""
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
        try:
            comando = recognizer.recognize_google(audio, language="pt-BR")
            return comando.lower()
        except sr.UnknownValueError:
            speak("Desculpe, não consegui entender. Pode repetir?")
            return ""
        except sr.RequestError:
            speak("Houve um problema ao acessar o serviço de reconhecimento de voz.")
            return ""

# Palavras-chave de comando
comandos_pesquisa = ["pesquisar por", "faça uma pesquisa", "procure por", "Jarves pesquise por", "Jarves procure por", "Jarves ´pesquisa pra mim"]
comandos_agenda = ["adicionar tarefa", "adicionar na agenda", "anote isso", "Jarves adicionar tarefa", "Jarves adicione"]
comandos_lembrete = ["definir lembrete", "criar lembrete", "me lembre de", "Jarves me lembre", "Jarves me lembre de", "Jarves anota um lembrete"]
comandos_saida = ["Sair", "Fechar", "Jarves encerra", "Jarves sair", "Jarves descansar", "Jarves boa noite"]
comandos_musica = ["Tocar", "Pesquise pela musica", "Musica", "Jarves tocar", "Jarves pesquise pela musica", "Jarves musica"]
comandos_previsao = [
    "Qual é a previsão do tempo?", 
    "Qual é o tempo de hoje?", 
    "Como está o tempo?", 
    "Como vai estar o tempo?", 
    "Qual é a previsão do clima?", 
    "Qual é a previsão do tempo para hoje?", 
    "Como vai estar o clima?", 
    "Está chovendo?", 
    "Vai chover hoje?", 
    "Qual a previsão para o tempo?", 
    "Jarves, qual é a previsão do tempo?", 
    "Jarves, qual é o tempo de hoje?", 
    "Jarves, como está o tempo?", 
    "Jarves, como vai estar o tempo?", 
    "Jarves, qual é a previsão do clima?", 
    "Jarves, qual é a previsão do tempo para hoje?", 
    "Jarves, como vai estar o clima?", 
    "Jarves, está chovendo?", 
    "Jarves, vai chover hoje?", 
    "Jarves, qual a previsão para o tempo?"
]
comandos_hora = [
    "Que horas são?", 
    "Me diga a hora", 
    "Qual é a hora?", 
    "Jarves, que horas são?", 
    "Jarves, me diga a hora", 
    "Jarves, qual é a hora?"
]

# Loop principal
speak("Olá Senhor, em que posso ser util?")
while True:
    comando = ouvir_comando()
    if comando:
        if any(frase in comando for frase in comandos_saida):
            speak("Até logo Senhor Xavier!")
            break
        pr.processar_comando(comando)