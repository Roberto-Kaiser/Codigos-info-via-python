import random

def gerar_id():
    return str(random.randint(1000000000, 9999999999))

print("--- Cadastro de Professor ---")

nome = input("Nome: ")

while True:
    idade = input("Idade: ")
    if idade.isdigit():
        break
    print("Idade deve conter apenas números!")

contato = input("Contato: ")
materias = input("Matéria(s): ")

while True:
    senha = input("Senha (máx 30 caracteres): ")
    if len(senha) <= 30:
        break
    print("Senha muito longa! Máximo 30 caracteres.")

id_professor = gerar_id()

print(f"\nCadastro concluído!")
print(f"ID: {id_professor}")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Contato: {contato}")
print(f"Matéria(s): {materias}")
print(f"Senha: {senha}")
