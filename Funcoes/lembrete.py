import datetime
import time

from main import speak

def definir_lembrete(mensagem, horario):
    """Função para definir um lembrete"""
    while True:
        horario_agora = datetime.datetime.now().strftime("%H:%M")
        if horario_agora == horario:
            speak(f"Lembrete: {mensagem}")
            break
        time.sleep(30)  # Verifica a cada 30 segundos

def horario():
    horario_agora = datetime.datetime.now().strftime("%H:%M")
    speak(f"No momento são {horario_agora}")