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


