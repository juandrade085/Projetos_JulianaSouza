import calendar
from datetime import date

print("ME DIGA SEU ANIVERSÁRIO")
dia_nascimento = int(input("DIA: "))
mes_nascimento = int(input("MÊS: "))
ano_nascimento = int(input("ANO: "))

calendar.setfirstweekday(calendar.SUNDAY) #Calendário começa no domingo
calendario = calendar.monthcalendar(ano_nascimento, mes_nascimento) #Estrutura do mês

nome_mes = calendar.month_name[mes_nascimento].capitalize()

#Título do calendário centralizado (34 espaços = 7 colunas x 4 + 6 espaços)
print(f"{nome_mes} {ano_nascimento}".center(34))

#Título dos dias da semana
dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
print(" ".join(f"{d:>4}" for d in dias_semana))

for semana in calendario:
    nova_semana = []
    for dia in semana:
        if dia == dia_nascimento:
            nova_semana.append(f"\033[0;31m{dia:>4}\033[m")  # dia do aniversário em vermelho
        elif dia == 0:
            nova_semana.append("    ")  # espaço para dias vazios
        else:
            nova_semana.append(f"{dia:>4}")
    print(" ".join(nova_semana))

# Data atual
hoje = date.today()
ano_atual = hoje.year

data_aniversario = date(ano_nascimento, mes_nascimento, dia_nascimento)
proximo_aniversario = date(ano_atual, mes_nascimento, dia_nascimento)

# Diferença entre a aniversário e hoje
if proximo_aniversario < hoje:
    diferenca = (hoje - proximo_aniversario).days
    print(f"Você já fez aniversário esse ano! Que legal!!!")
    print(f"Foi há {diferenca} dias.")

elif proximo_aniversario > hoje:
    diferenca = (proximo_aniversario - hoje).days
    print(f"Falt{'a' if diferenca == 1 else 'am'} {diferenca} dia{'s' if diferenca > 1 else ''} para o seu aniversário!")
else:
    # aniversário sendo na data atual
    print(f"🎉🎂 Seu aniversário é HOJE !!!🎁🥳"
          f"\n✨✨✨PARABÉNS✨✨✨")