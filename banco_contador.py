# Contador de alunos aprovados nas provas
banco_alunos = {
    "Nome": "Carlos", "nota": 6.5},{
    "Nome": "Marcos", "nota": 7.0},{
    "Nome": "Ana", "nota": 9.0},{
    "Nome": "Maria", "nota": 4.5}
contador = 0
for aluno in banco_alunos:
    if aluno["nota"] >= 7:
        contador += 1
        print(aluno["Nome"], "foi aprovado")
print("O total de alunos aprovados foi de:", contador)

