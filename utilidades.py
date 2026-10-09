def media_notas(notas):
       return sum(notas) / len(notas)
print(round(media_notas([7, 8, 9]), 2))
def desconto(preco, percentual= 10):
 return preco - preco * percentual / 100
print(desconto(200))
print(desconto(200, 25))
def situacao(media):
    if media >= 5:
        return "Aprovado"
    else:
        return "Reprovado"
print(situacao(7))
