import sqlite3
import shutil
from datetime import datetime, timedelta
import os

def fazer_backup(db, directory):
    data_atual = datetime.now()
    nome_backup = f"{db}_{data_atual.strftime('%Y-%m-%d')}.db"
    caminho_db = os.path.join(directory, db)
    caminho_backup = os.path.join(directory, nome_backup)
    shutil.copy(caminho_db, caminho_backup)
    print(f"Backup do banco de dados criado em: {caminho_backup}")
    return data_atual

def verificar_diretorio_backup(directory):
    try:    
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Diretório de backup criado em: {directory}")
        else:
            print(f"Diretório de backup encontrado em: {directory}")
    except Exception as err:
        print(f'Log Backup ultimo backup: {err}')

def backup_drive(directory, arquivo_backup):
    try:
        shutil.move(os.path.join(directory, arquivo_backup), os.path.join(destino_drive, arquivo_backup))
        print(f"Backup movido para o drive: {os.path.join(destino_drive, arquivo_backup)}")
    except Exception as e:
        print(f"Erro ao mover backup para o drive: {e}")

def limpar_backup_antigos(directory, max_backups):
    list_backups = []
    for arquivo in os.listdir(directory):
        if arquivo.startswith("clientes.db_") and arquivo.endswith(".db"):
            list_backups.append(arquivo)
    
    list_backups.sort(reverse=True)
    backups = list_backups[:max_backups]

    for arquivo in list_backups:
        if arquivo not in backups:
            caminho_arquivo = os.path.join(directory, arquivo)
            backup_drive(directory, arquivo)
            os.remove(caminho_arquivo)
            print(f"46 Backup anterior removido: {caminho_arquivo}")

def verificar_data_ultimo_backup(directory):
    try:    
        backups = []
        for arquivo in os.listdir(directory):
            if arquivo.startswith("clientes.db_") and arquivo.endswith(".db"):
                backups.append(arquivo)
        if backups:
            ultimo_backup = max(backups)
            data_backup_str = ultimo_backup.split('_')[1].split('.')[0]
            return datetime.strptime(data_backup_str, '%Y-%m-%d').date()
        else:
            data_temp = "2024-04-15"
            data = datetime.strptime(data_temp, "%Y-%m-%d").date()
            return data
    except Exception as err:
        print(f'60 Log Backup ultimo backup: {err}')

def main():
    db = "clientes.db"
    diretorio_backup = os.getcwd()
    maximo_backups = 4

    verificar_diretorio_backup(diretorio_backup)
    data_ultimo_backup = verificar_data_ultimo_backup(diretorio_backup)
    data_atual = datetime.now().date()

    if (data_atual - data_ultimo_backup).days >= 7:
        data_ultimo_backup = fazer_backup(db, diretorio_backup)
        limpar_backup_antigos(diretorio_backup, maximo_backups)

if __name__ == "__main__":
    main()
    