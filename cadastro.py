cadastro ={
    "nome": "Wilson","idade": 65,
    "cidade": "Florianópolis",
    "profissão": "engenheiro"}
cadastro.update({"e-mail": "wilson_de-souza@estudante.sesisenai.org.br"})
print(cadastro)
for chave, valor in cadastro.items():
    print(chave, ":", valor)