# SISTEMA


from modulos_uteis.funcoes_cadastro import *

from modulos_uteis.funcoes_decoracao import *

# Exibe o cabeçalho decorado

cabecalho ('CLÍNICA VIDA+')


while True:
    resposta = menu(['Cadastros', 'Agendamentos', 'Relatórios', 'Sair do Sistema'])

    if resposta == 1:
        while True:
            sub_resposta = menu(['Cadastro de Pacientes', 'Cadastro de Médicos', 'Cadastro de Exames', 'Voltar'], titulo='CADASTROS')
            if sub_resposta == 1:
                cabecalho('NOVO PACIENTE - CADASTRO')
                paciente = cadastro_paciente()
                if paciente:
                    print(f"Paciente {paciente['nome']} {paciente['sobrenome']} cadastrado(a) com sucesso!")
                else:
                    print("❌ Cadastro falhou. Verifique os dados e tente novamente.")
                print(f"Paciente {paciente['nome']} {paciente['sobrenome']} cadastrado(a) com sucesso!")
            elif sub_resposta == 2:
                cabecalho('NOVO MÉDICO - CADASTRO')
                medico = cadastro_medico()
                print(f"Médico {medico['nome']} {medico['sobrenome']} cadastrado(a) com sucesso!")
            elif sub_resposta == 4:
                break  # Volta para o Menu Principal

            continuar = ''
            while continuar not in 'SN':
                continuar = input('Deseja continuar em CADASTROS? [S/N] ').strip().upper()[0]
            if continuar == 'N':
                break
"""elif sub_resposta == 3:
    cabecalho('NOVO EXAME - CADASTRO')
    exame = cadastro_exame()
    print(f"Exame {exame['tipo']} cadastrado com sucesso!")
    elif resposta == 2:
        cabecalho('AGENDAMENTOS')
        # lógica de agendamentos aqui
        continuar = ''
        while continuar not in 'SN':
            continuar = input('Deseja realizar outra ação em AGENDAMENTOS? [S/N] ').strip().upper()[0]
        if continuar == 'N':
            continue  # volta ao menu principal

    elif resposta == 3:
        cabecalho('RELATÓRIOS')
        # lógica de relatórios aqui
        continuar = ''
        while continuar not in 'SN':
            continuar = input('Deseja realizar outra ação em RELATÓRIOS? [S/N] ').strip().upper()[0]
        if continuar == 'N':
            continue  # volta ao menu principal

    elif resposta == 4:
        cabecalho('Saindo do Sistema... Até logo!')
        break"""



"""   
    elif resposta == 2:
        cabecalho ('AGENDAMENTOS')
        # Função de agendamento (a ser implementada)
        print("Função de agendamento ainda não implementada.")
    elif resposta == 3:
        cabecalho ('RELATÓRIOS')
        # Função de relatórios (a ser implementada)
        print("Função de relatórios ainda não implementada.")
    elif resposta == 4:
        cabecalho ('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')


    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa',
                     'Sair do Sistema'])
    if resposta == 1:
        cabecalho ('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq_pacientes.txt, nome, idade)
    elif resposta == 2:
        # Opção de listar conteúdo de um arquivo
        lerArquivo(arq)        
    elif resposta == 3:
        cabecalho ('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')"""

