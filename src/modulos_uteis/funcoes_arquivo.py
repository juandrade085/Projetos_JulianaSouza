from modulos_uteis.funcoes_decoracao import cabecalho,menu_especialidades_medicas
from modulos_uteis.funcoes_constantes import ARQ_MEDICOS, ARQ_EXAMES
import csv
import os

def arquivo_existe(nome):
    return os.path.isfile(nome)

def salvar_csv(nome_arquivo, dados, cabecalho=None):
    existe = arquivo_existe(nome_arquivo)
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arq:
        writer = csv.writer(arq)
        if not existe and cabecalho:
            writer.writerow(cabecalho)
        writer.writerow(dados)

def ler_csv(nome_arquivo):
    if not arquivo_existe(nome_arquivo):
        return []
    with open(nome_arquivo, 'r', encoding='utf-8') as arq:
        reader = csv.DictReader(arq)
        return list(reader)
