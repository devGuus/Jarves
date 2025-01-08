import requests

from main import speak

def obter_previsao(cidade):
    # codigicação da cidade 
    cidade_codificada = cidade.replace(" ", "-").lower()

    url = f"https://www.metaweather.com/api/location/search/?query={cidade_codificada}"

    try: 
        resposta = requests.get(url)
        dados = resposta.json()

        if not dados:
            return speak(f"Desculpe senhor, não há informações disponiveis no momento sobre a cidade de {cidade}.")
        
        woeid = dados[0]['woeid']

        url_previsao = f"https://www.metaweather.com/api/location/{woeid}/"
        resposta_previsao = requests.get(url_previsao)
        dados_previsao = resposta_previsao.json()

        # Pegando as informações da previsão (os dados retornam como uma lista com as previsões do dia)
        previsao = dados_previsao['consolidated_weather'][0]

        descricao = previsao['weather_state_name']
        temperatura = previsao['the_temp']
        umidade = previsao['humidity']

        jarves_responde = speak(f"A previsão do tempo para {cidade} é: {descricao}. A temperatura atual é de {temperatura:.1f} graus Celsius, com uma umidade de {umidade}%.")
        return jarves_responde
    
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API: {str(e)}"
    except KeyError as e:
        return f"Erro ao processar os dados da previsão: {str(e)}"