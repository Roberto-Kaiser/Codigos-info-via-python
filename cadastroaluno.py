import random

def gerar_id():
    return str(random.randint(1000000000, 9999999999))

print("--- Cadastro de Aluno ---")

nome = input("Nome: ")

while True:
    idade = input("Idade: ")
    if idade.isdigit():
        break
    print("Idade deve conter apenas números!")

while True:
    serie = input("Série (máx 3 caracteres): ")
    if len(serie) <= 3:
        break
    print("Série deve ter no máximo 3 caracteres!")

while True:
    senha = input("Senha (máx 30 caracteres): ")
    if len(senha) <= 30:
        break
    print("Sua senha deve conter no máximo 30 caracteres.")

id_aluno = gerar_id()

print(f"\nCadastro concluído!")
print(f"ID: {id_aluno}")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Série: {serie}")
print(f"Senha: {senha}")
