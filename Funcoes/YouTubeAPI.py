import yt_dlp

def pesquisar_musica(query):
    # configurações
    yt_opcoes = {
        'quiet': True,
        'extract_flat': True, # Não fazer download
    }
    with yt_dlp.YoutubeDL(yt_opcoes) as search:
        result = search.extract_info(f"ytsearch5:{query}", download=False)
        for entry in result['entries']:
            print(f'Titulo: {entry["title"]}')
            print(f'URL: {entry["url"]}')
            print("--- --- --- --- --- ---")

# Download de vídeos 
# yt_opcoes = {
#     'format': 'best',  # Baixa a melhor qualidade
# }
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['URL_DO_VIDEO'])

# Baixar áudio MP3
# ydl_opts = {
#     'format': 'best',  # Baixa a melhor qualidade
# }
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['URL_DO_VIDEO'])

# Baixar as legendas caso o vídeo possua
# ydl_opts = {
#     'writesubtitles': True,  # Baixa as legendas
#     'subtitleslangs': ['en'],  # Idioma das legendas
# }
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['URL_DO_VIDEO'])