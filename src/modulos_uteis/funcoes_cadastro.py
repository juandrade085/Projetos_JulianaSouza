# FUNÇÕES DE CADASTRO
"""NUNCA MODIFIICAR - VAI QUEBRAR CÓDIGOS COMO:
 - projeto_gestao_hospitalar.py"""


from modulos_uteis.funcoes_decoracao import cabecalho,menu_especialidades_medicas
from modulos_uteis.funcoes_arquivo import salvar_csv, ler_csv, arquivo_existe
from modulos_uteis.funcoes_constantes import ARQ_MEDICOS, ARQ_EXAMES
from datetime import datetime, date
import csv
import os



# DATA E HORA ATUAL

def calcular_idade_e_dias(data_nascimento_str):
    try:
        nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
        hoje = date.today()

        # Cálculo da idade

        idade = hoje.year - nascimento.year
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1

        # Último aniversário

        ultimo_aniversario = nascimento.replace(year=hoje.year)
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            ultimo_aniversario = nascimento.replace(year=hoje.year - 1)

        dias_com_idade_nova = (hoje - ultimo_aniversario).days
        return idade, dias_com_idade_nova

    except ValueError:
        return None, None

def cadastro_paciente():
    try:
        # Validação do nome
        while True:
            nome_paciente = input("Nome do Paciente: ").strip().title()
            if nome_paciente.replace(" ", "").isalpha():
                break
            print("❌ Nome inválido. Digite apenas letras.")

        # Validação do sobrenome
        while True:
            sobrenome_paciente = input("Sobrenome do Paciente: ").strip().title()
            if sobrenome_paciente.replace(" ", "").isalpha():
                break
            print("❌ Sobrenome inválido. Digite apenas letras.")

        # Validação da data de nascimento
        while True:
            data_nascimento_paciente_str = input("Data de Nascimento (dd/mm/aaaa): ").strip()
            if not data_nascimento_paciente_str:
                print("❌ Data de nascimento não pode estar vazia.")
                continue

            idade, dias_com_idade_nova = calcular_idade_e_dias(data_nascimento_paciente_str)
            if idade is None:
                print("❌ Data inválida. Use o formato dd/mm/aaaa.")
                continue

            nascimento = datetime.strptime(data_nascimento_paciente_str, "%d/%m/%Y").date()
            if nascimento > date.today():
                print("❌ Data de nascimento não pode ser no futuro.")
                continue

            break

        return {
            "nome_paciente": nome_paciente,
            "sobrenome_paciente": sobrenome_paciente,
            "idade": idade,
            "dias_com_idade_nova": dias_com_idade_nova
        }

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def cadastro_medico():
    nome_medico = input("Nome do Médico: ").title()
    sobrenome_medico = input("Sobrenome do Médico: ").title()

    while True:
        escolha, opcoes_especialidades = menu_especialidades_medicas()
        if escolha == len(opcoes_especialidades):
            print("🔙 Retornando ao menu anterior...")
            return
        elif 1 <= escolha < len(opcoes_especialidades):
            especialidade = opcoes_especialidades[escolha - 1]
            break
        else:
            print("❌ Especialidade inválida. Tente novamente.")

    salvar_csv(ARQ_MEDICOS, [nome_medico, sobrenome_medico, especialidade],
               cabecalho=["nome_medico", "sobrenome_medico", "especialidade"])    
    return {
        "nome_medico": nome_medico,
        "sobrenome_medico": sobrenome_medico,
        "especialidade": especialidade
    }

def cadastro_exame():
    nome_exame = input("Nome do Exame: ").title()
    medicos = ler_csv(ARQ_MEDICOS)

    if not medicos:
        print("❌ Nenhum médico cadastrado. Cadastre um médico primeiro.")
        return

    print("\nMédicos disponíveis:")
    for i, m in enumerate(medicos, start=1):
        print(f"{i} - Dr(a). {m['nome']} {m['sobrenome']} ({m['especialidade']})")

    escolha = int(input("Escolha o médico solicitante: "))
    if not (1 <= escolha <= len(medicos)):
        print("❌ Opção inválida.")
        return

    medico_escolhido = medicos[escolha - 1]

    salvar_csv(ARQ_EXAMES,
               [nome_exame, medico_escolhido['nome'], medico_escolhido['sobrenome'], medico_escolhido['especialidade']],
               cabecalho=["nome_exame", "nome_medico", "sobrenome_medico", "especialidade"])
    return {
        "nome_exame": nome_exame,
    }

def continuar(opcao):
    while True:
        resp = input(f'Quer continuar em {opcao}? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            return resp
        print('ERRO! Responda apenas S ou N.')


