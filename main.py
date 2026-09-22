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
