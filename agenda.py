# Criação de uma agenda com 5 nomes e com nova branch 
contatos = []
def adicionar(nome,telefone):
    contatos.append({"nome": nome, "telefone": telefone})
adicionar("Ana", "48 9999-0001")
adicionar("Bruno", "48 9999-0002")
for contato in contatos:
    print(contato["nome"], contato["telefone"])
