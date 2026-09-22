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

# Busca um medicamento pelo nome
def buscar_medicamento(medicamentos, nome):

    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            return medicamento

    return None


# Mostra somente o estoque dos medicamentos
def mostrar_estoque(medicamentos):

    if len(medicamentos) == 0:
        print("\nNenhum medicamento cadastrado.")
        return

    print("\n=== ESTOQUE DE MEDICAMENTOS ===")

    for medicamento in medicamentos:
        print(
            f"{medicamento['nome']} - "
            f"{medicamento['quantidade']} unidades"
        )

# Menu principal
def menu():

    # Carrega os dados do arquivo quando o programa inicia
    medicamentos = carregar_medicamentos()

    while True:

        print("\n===== SISTEMA DA FARMÁCIA =====")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Buscar medicamento")
        print("4 - Mostrar estoque")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_medicamento(medicamentos)

        elif opcao == "2":
            listar_medicamentos(medicamentos)

        elif opcao == "3":
            nome = input("Digite o nome do medicamento: ")

            resultado = buscar_medicamento(medicamentos, nome)

            if resultado:
                print("\nMedicamento encontrado!")
                print("Nome:", resultado["nome"])
                print("Categoria:", resultado["categoria"])
                print("Quantidade:", resultado["quantidade"])
            else:
                print("\nMedicamento não encontrado.")

        elif opcao == "4":
            mostrar_estoque(medicamentos)

        elif opcao == "5":
            # Salva os dados antes de encerrar o programa
            salvar_medicamentos(medicamentos)
            print("\nDados salvos. Programa encerrado.")
            break

        else:
            print("\nOpção inválida!")


# Inicia o programa
menu()
