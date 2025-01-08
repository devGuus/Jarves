from main import agenda
from main import speak

def adicionar_na_agenda(tarefa):
    """Função para adicionar tarefa à agenda"""
    agenda.append(tarefa)
    speak(f"Tarefa {tarefa} adicionada à sua agenda.")

def exibir_agenda():
    """Função para exibir as tarefas da agenda"""
    if agenda:
        speak("Aqui estão suas tarefas:")
        for i, tarefa in enumerate(agenda, start=1):
            speak(f"Tarefa {i}: {tarefa}")
    else:
        speak("Sua agenda está vazia.")