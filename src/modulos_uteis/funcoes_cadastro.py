# FUNÇÕES DE CADASTRO
"""NUNCA MODIFIICAR - VAI QUEBRAR CÓDIGOS COMO:
 - projeto_gestao_hospitalar.py"""



from modulos_uteis.funcoes_decoracao import cabecalho
from datetime import datetime, date

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

def arquivoExiste (nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass
    except Exception as erro:
        print(f'Houve um ERRO na criação do arquivo!Erro: {erro}')
    else:
        print(f'Arquivo {nome} criado com sucesso!!!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'Houve um ERRO ao ler o arquivo!Erro: {erro}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a: #pra cada linha no arquivo
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:<3} anos')

    finally:
        a.close()

def cadastro_paciente():
    try:
        while True:
            nome = input("Nome do Paciente: ").strip().title()
            if nome.replace(" ", "").isalpha(): # VERIFICAÇÃO NOME
                break
            print("❌ Nome inválido. Digite apenas letras.")

        # 🔹 Validação do sobrenome
        while True:
            sobrenome = input("Sobrenome do Paciente: ").strip().title()
            if sobrenome.replace(" ", "").isalpha(): # VERIFICAÇÃO SOBRENOME
                break
            print("❌ Sobrenome inválido. Digite apenas letras.")

        # 🔹 Validação da data de nascimento
        while True:
            data_nascimento_str = input("Data de Nascimento (dd/mm/aaaa): ").strip()
            if not data_nascimento_str:
                print("❌ Data de nascimento não pode estar vazia.") # VERIFICAÇÃO DATA DE NASCIMENTO
                continue

            idade, dias_com_idade_nova = calcular_idade_e_dias(data_nascimento_str)
            if idade is None:
                print("❌ Data inválida. Use o formato dd/mm/aaaa.") # VERIFICAÇÃO IDADE
                continue

            nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
            if nascimento > date.today():
                print("❌ Data de nascimento não pode ser no futuro.") # VERIFICAÇÃO DATA FUTURA
                continue

            break
        return {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "dias_com_idade_nova": dias_com_idade_nova
        }

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def cadastro_medico():
    nome = input("Nome do Médico: ").title()
    sobrenome = input("Sobrenome do Paciente: ").title()
    Espacialidade = input("Espacialidade: ").title()
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "espacialidade" : Espacialidade
    }
