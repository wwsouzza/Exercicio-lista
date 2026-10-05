# Criação de uma agenda com 5 nomes e com nova branch 
contatos = []
def adicionar(nome,telefone):
    contatos.append({"nome": nome, "telefone": telefone})
adicionar("Ana", "48 9999-0001")
adicionar("Bruno", "48 9999-0002")
adicionar("Carlos", "48 9999-0003")
adicionar("João", "48 9999-0004")
adicionar("Sergio", "48 9999-0005")
for contato in contatos:
    print(contato["nome"], contato["telefone"])
nome_desejado = input("digite o nome do contato que deseja: ")
for contato in contatos:
    if contato["nome"] == nome_desejado:
        print("Telefone do contato:", contato["telefone"])
        break
      