alunos = [
    {"nome": "Fabio", "nota": 9.0},
    {"nome": "Luis", "nota": 6.5},
    {"nome": "Mario", "nota": 7.0},
    {"nome": "Paulo", "nota": 5.5},
    {"nome": "Chico", "nota": 8.2},
]
ordenados = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)
print("Do maior para o menor:")
for aluno in ordenados:
    print("-", aluno["nome"], aluno["nota"])
aprovados = list(filter(lambda aluno: aluno["nota"] >= 7, alunos))
print("Aprovados:", [aluno["nome"] for aluno in aprovados])