# SISTEMA

from modulos_uteis.funcoes_cadastro import cadastro_paciente, cadastro_medico, cadastro_exame, continuar
from modulos_uteis.funcoes_decoracao import cabecalho, menu, menu_especialidades_medicas
from modulos_uteis.funcoes_arquivo import salvar_csv, ler_csv
import os


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
                    print(f"✅ Paciente {paciente['nome_paciente']} {paciente['sobrenome_paciente']} cadastrado(a) com sucesso!")
                else:
                    print("❌ Cadastro falhou. Verifique os dados e tente novamente.")
                if continuar(nome_opcao)  == 'N':
                    print('Retornando ao menu principal...')
                    break  # Sai do loop e volta ao menu principal

            elif sub_resposta == 2:
                cabecalho('NOVO MÉDICO - CADASTRO')
                medico = cadastro_medico()
                if medico:
                    print(f"✅ Médico(a) {medico['nome_medico']} {medico['sobrenome_medico']} - {medico['especialidade']} cadastrado(a) com sucesso!")
                    if continuar(nome_opcao) == 'N':
                        print('Retornando ao menu principal...')
                        break
                else:
                    print("🔙 Cadastro cancelado. Retornando ao menu de cadastros...")
            elif sub_resposta == 3:
                cabecalho('NOVO EXAME - CADASTRO')
                exame = cadastro_exame()
                if medico:
                    print(f"✅ Exame {exame['nome_exame']} da especialidade {menu_especialidades_medicas} -  cadastrado(a) com sucesso!")
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

    elif resposta == 4:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print("❌ Opção inválida. Tente novamente.")