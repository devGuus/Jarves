import wikipedia
import pywhatkit
import webbrowser

from main import speak

def pesquisar_na_web(termo):
    """Função para pesquisar na web"""
    url = f"https://www.google.com/search?q={termo}"
    webbrowser.open(url)
    speak(f"Pesquisando por {termo} no Google.")