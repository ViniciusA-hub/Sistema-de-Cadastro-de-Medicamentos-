import csv
import os

ARQUIVO = "medicamentos.csv"
# Carrega os medicamentos do arquivo
def carregar_medicamentos():
    medicamentos = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                linha["quantidade"] = int(linha["quantidade"])
                medicamentos.append(linha)

    return medicamentos

# Salva todos os medicamentos no arquivo
def salvar_medicamentos(medicamentos):
    with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "categoria", "quantidade"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()

        for medicamento in medicamentos:
            escritor.writerow(medicamento)
# Cadastra um medicamento
def cadastrar_medicamento(medicamentos):
    nome = input("Nome do medicamento: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade em estoque: "))

    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }

    medicamentos.append(medicamento)

    print("\nMedicamento cadastrado com sucesso!")
    
# Lista os medicamentos
def listar_medicamentos(medicamentos):

    if len(medicamentos) == 0:
        print("\nNenhum medicamento cadastrado.")
        return

    print("\n=== LISTA DE MEDICAMENTOS ===")

    for medicamento in medicamentos:
        print("-----------------------------")
        print("Nome:", medicamento["nome"])
        print("Categoria:", medicamento["categoria"])
        print("Quantidade:", medicamento["quantidade"])