import random

def gerar_id_sessao():
    return str(random.randint(100000, 999999))

print("--- Agendamento de Sessão ---")

id_sessao = gerar_id_sessao()
motivos = input("Motivos da sessão: ")
professores = input("Professor(es) envolvidos: ")
pedagogas = input("Pedagoga(s) envolvidas: ")
alunos = input("Aluno(s)/Turma(s) envolvidos(as): ")

while True:
    data = input("Data (DDMMAAAA): ")
    if data.isdigit() and len(data) == 8:
        break
    print("Data deve conter 8 números no formato DDMMAAAA!")

while True:
    horario = input("Horário (HHMM): ")
    if horario.isdigit() and len(horario) == 4:
        break
    print("Horário deve conter 4 números no formato HHMM!")

local = input("Local da sessão: ")

print(f"\nSessão agendada!")
print(f"ID da Sessão: {id_sessao}")
print(f"Motivos: {motivos}")
print(f"Professor(es): {professores}")
print(f"Pedagoga(s): {pedagogas}")
print(f"Aluno(s)/Turma(s): {alunos}")
print(f"Data: {data[:2]}/{data[2:4]}/{data[4:]}") 
print(f"Horário: {horario[:2]}:{horario[2:]}")    
print(f"Local: {local}")
