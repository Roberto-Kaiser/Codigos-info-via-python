import random

def gerar_id_turma():
    return str(random.randint(1000000000, 9999999999))

print("--- Cadastro de Turma ---")

id_turma = gerar_id_turma()

while True:
    quantidade_alunos = input("Quantidade de alunos: ")
    if quantidade_alunos.isdigit():
        break
    print("Use apenas números!")

while True:
    serie = input("Série: ")
    if len(serie) <= 3:
        break
    print("Use no máximo 3 caracteres!")

print(f"\nTurma cadastrada com sucesso!")
print(f"ID da Turma: {id_turma}")
print(f"Quantidade de Alunos: {quantidade_alunos}")
print(f"Série: {serie}")
