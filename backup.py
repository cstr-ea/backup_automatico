import os
import shutil
from datetime import datetime

def criar_pasta_backup(destino):
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho_backup = os.path.join(destino, f"backup_{data_atual}")
    
    if not os.path.exists(caminho_backup):
        os.makedirs(caminho_backup)
    
    return caminho_backup

def realizar_backup(origem, destino):
    if not os.path.exists(origem):
        print("Diretório de origem não encontrado.")
        return

    pasta_backup = criar_pasta_backup(destino)

    for raiz, dirs, arquivos in os.walk(origem):
        for arquivo in arquivos:
            caminho_origem = os.path.join(raiz, arquivo)

            # Mantém estrutura de pastas
            caminho_relativo = os.path.relpath(raiz, origem)
            pasta_destino = os.path.join(pasta_backup, caminho_relativo)

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            caminho_destino = os.path.join(pasta_destino, arquivo)

            shutil.copy2(caminho_origem, caminho_destino)

    print(f"Backup concluído com sucesso em: {pasta_backup}")

# Configuração
origem = input("Digite o caminho da pasta de origem: ")
destino = input("Digite o caminho da pasta de destino: ")

realizar_backup(origem, destino)
