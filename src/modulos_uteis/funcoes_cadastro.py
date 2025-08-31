# FUNÇÕES DE CADASTRO

def cadastro():
    nome = input("Nome do Paciente: ")
    sobrenome = input("Sobrenome do Paciente: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")

    def calcular_idade_e_dias(data_nascimento):
        from datetime import datetime, date
        try:
            nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            hoje = date.today()

            # Cálculo da idade
            idade = hoje.year - nascimento.year
            if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
                idade -= 1

            # Último aniversário
            ultimo_aniversario = nascimento.replace(year=hoje.year)
            if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
                ultimo_aniversario = nascimento.replace(year=hoje.year - 1)

            # Dias desde o último aniversário
            dias_com_idade_nova = (hoje - ultimo_aniversario).days

            return idade, dias_com_idade_nova
        except ValueError:
            return "Data inválida", None

    idade, dias_com_idade_nova = calcular_idade_e_dias(data_nascimento)

    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "data_nascimento": data_nascimento,
        "idade": idade,
        "dias_com_idade_nova": dias_com_idade_nova
    }
