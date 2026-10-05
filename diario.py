contador = 0
with open("diario.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
       contador += 1
       print (contador,linha.strip())