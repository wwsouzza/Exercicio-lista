import csv
import re

with open("contatos.csv", newline="", encoding="utf-8") as f:
    for contato in csv.DictReader(f):
        original = contato["telefone"]
        so_digitos = re.sub(r"\D", "", original)  # remove tudo que não é dígito
        valido = re.fullmatch(r"\d{11}", so_digitos)  
        situacao = "válido" if valido else "inválido"
        print(contato["nome"], "|", original, "->", so_digitos, "|", situacao)