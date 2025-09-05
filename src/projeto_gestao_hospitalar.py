# SISTEMA


from modulos_uteis.funcoes_cadastro import *

from modulos_uteis.funcoes_decoracao import *

# Exibe o cabeçalho decorado

cabecalho ('CLÍNICA VIDA+')


while True:
    resposta = menu(['Cadastros', 'Agendamentos', 'Relatórios', 'Sair do Sistema'])

    if resposta == 1:
        nome_opcao = 'Cadastros'
        while True:
            sub_resposta = menu(
                ['Cadastro de Pacientes', 'Cadastro de Médicos', 'Cadastro de Exames', 'Voltar'],
                titulo='CADASTROS'
            )
            if sub_resposta == 1:
                cabecalho('NOVO PACIENTE - CADASTRO')
                paciente = cadastro_paciente()
                if paciente:
                    print(f"✅ Paciente {paciente['nome']} {paciente['sobrenome']} cadastrado(a) com sucesso!")
                else:
                    print("❌ Cadastro falhou. Verifique os dados e tente novamente.")
                if continuar(nome_opcao)  == 'N':
                    print('Retornando ao menu principal...')
                    break  # Sai do loop e volta ao menu principal

            elif sub_resposta == 2:
                arquivo_csv = "basededados_medicos.csv"
                if os.path.exists(arquivo_csv):
                    print("O arquivo já existe. Vamos apenas adicionar novos médicos.")
                else:
                    print(f"Criando '{arquivo_csv}'...")
                cabecalho('NOVO MÉDICO - CADASTRO')
                medico = cadastro_medico()
                if medico:
                    print(f"✅ Médico {medico['nome']} {medico['sobrenome']} - {medico['especialidade']} cadastrado(a) com sucesso!")
                    if continuar(nome_opcao) == 'N':
                        print('Retornando ao menu principal...')
                        break
                else:
                    print("🔙 Cadastro cancelado. Retornando ao menu de cadastros...")
            elif sub_resposta == 3:
                cabecalho('NOVO EXAME - CADASTRO')
                medico = cadastro_medico()
                if medico:
                    print(f"✅ Médico {medico['nome']} {medico['sobrenome']} - {medico['especialidade']} cadastrado(a) com sucesso!")
                    if continuar(nome_opcao) == 'N':
                        print('Retornando ao menu principal...')
                        break
                else:
                    print("🔙 Cadastro cancelado. Retornando ao menu de cadastros...")

            elif sub_resposta == 4:
                break  # Volta para o Menu Principal

            elif resposta == 4:
                cabecalho('Saindo do Sistema... Até logo!')
                break

    if resposta == 3:
        cabecalho('RELATÓRIOS - EM CONSTRUÇÃO')
        nome_opcao = 'Cadastros'
        while True:
            sub_resposta = menu(
                ['Relatórios de Pacientes', 'Relatórios de Médicos', 'Relatórios de Exames', 'Voltar']
                titulo = 'nome_opcao'
            )
            if sub_resposta == 1:
                print("🔧 Esta funcionalidade está em construção. Por favor, volte mais tarde.")
            if continuar(nome_opcao) == 'N':
                print('Retornando ao menu principal...')
