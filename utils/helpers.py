import os
from jogoteca import app

def recupera_imagem(id):
    nome = f'capa{id}.jpg'
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if nome_arquivo == nome:
            return nome_arquivo

    return 'capa_padrao.jpg'