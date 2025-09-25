import random

def gerar_id():
    return str(random.randint(1000000000, 9999999999))

print("--- Cadastro de Diretor ---")

nome = input("Nome: ")

while True:
    idade = input("Idade: ")
    if idade.isdigit():
        break
    print("Idade deve conter apenas números!")

contato = input("Contato: ")

while True:
    senha = input("Senha (máx 30 caracteres): ")
    if len(senha) <= 30:
        break
    print("Senha muito longa! Máximo 30 caracteres.")

id_diretor = gerar_id()

print(f"\nCadastro concluído!")
print(f"ID: {id_diretor}")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Contato: {contato}")
print(f"Senha: {senha}")
