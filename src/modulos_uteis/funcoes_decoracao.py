# FUNÇÕES DE DECORAÇÃO
"""NUNCA MODIFIICAR - VAI QUEBRAR CÓDIGOS COMO:
 - projeto_gestao_hospitalar.py
 - funcoes_cadastro.py"""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def decoracao(item='-=', tamanho=20):
    return item * tamanho

def cabecalho(txt):
    largura = len(txt) + 6  # margem extra para respiro visual
    print(decoracao('-=', largura // len('-=')))  # ajusta para o número de repetições
    print(txt.center(largura))
    print(decoracao('-=', largura // len('-=')))

def menu(lista, titulo='MENU PRINCIPAL'):
    cabecalho(titulo)
    for i, item in enumerate(lista, start=1):
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
    print(decoracao())
    return leiaInt('\033[32mSua Opção:\033[m ')
