import re
from datetime import datetime

def so_digitos(texto):
    """Remove tudo que não for dígito."""
    return re.sub(r"\D", "", texto)

def normalizar_nome(nome):
    """Tira espaços extras e padroniza a caixa (Title Case)."""
    return " ".join(nome.split()).title()

def formatar_data(texto):
    """Converte dd/mm/aaaa para AAAA-MM-DD."""
    return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")

if __name__ == "__main__":
    print(so_digitos("(48) 93456-7445"))        
    print(normalizar_nome("  Flavio   SILVA "))    
    print(formatar_data("08/04/2023"))         