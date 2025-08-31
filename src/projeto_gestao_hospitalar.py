# SISTEMA


import modulos_uteis.funcoes_cadastro as fc

paciente = fc.cadastro()

"""from funcoes_decoracao import decoracao as dec


# Exibe o cabeçalho decorado
print(dec(15, '-='))
print(f"{'CLÍNICA VIDA+':^30}")
print(dec(15, '-='))"""

# Realiza o cadastro do paciente


# Exibe os dados do paciente cadastrado
print(
    f"Paciente: {paciente['nome']} {paciente['sobrenome']}, "
    f"{paciente['idade']} anos e {paciente['dias_com_idade_nova']} dias — cadastrado com sucesso!"
)