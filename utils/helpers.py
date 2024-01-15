import os

from jogoteca import app


def recupera_imagem(id):
    nome = f'capa{id}'
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if nome in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        caminho_arquivo = os.path.join(app.config['UPLOAD_PATH'], arquivo)
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
