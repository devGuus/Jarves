from main import *

def processar_comando(comando):
    """Processa o comando de voz"""
    # Pesquisa Web
    if any(frase in comando for frase in comandos_pesquisa):
        termo = comando.replace("pesquisar por", "").strip()
        termo = termo.replace("faça uma pesquisa", "").strip()
        termo = termo.replace("procure por", "").strip()
        wb.pesquisar_na_web(termo)
    # Agendar
    elif any(frase in comando for frase in comandos_agenda):
        tarefa = comando.replace("adicionar tarefa", "").strip()
        tarefa = tarefa.replace("adicionar na agenda", "").strip()
        tarefa = tarefa.replace("anote isso", "").strip()
        ag.adicionar_na_agenda(tarefa)
    # Agendar um lembrete
    elif any(frase in comando for frase in comandos_lembrete):
        speak("Que mensagem ponho no lembrete senhor?")
        mensagem = ouvir_comando()
        speak("Qual horário?")
        horario = ouvir_comando()
        speak(f"Lembrete para {mensagem} às {horario} anotado senhor.")
        lem.definir_lembrete(mensagem, horario)
    # Pedir musica
    elif any(frase in comando for frase in comandos_musica):
        speak("O que o senhor deseja ouvir hoje?")
        musica = ouvir_comando()
        speak(f"Procurando musica", {musica})
        ytf.pesquisar_musica(musica)
    # Previsao do tempo
    elif any(frase in comando for frase in comandos_previsao):
        speak("Qual cidade deseja saber a previsão Senhor?")
        cidade = ouvir_comando()
        temp.obter_previsao(cidade)
    # Horario atual
    elif any(frase in comando for frase in comandos_hora):
        lem.horario()
    else:
        speak("Peço perdão Senhor, mas não reconheci o comando.")