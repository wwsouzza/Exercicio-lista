# Iremos verificar se o ano é bissexto ou não
def e_bissexto(ano):
    """Devolve True se o ano for bissexto e False se não for."""
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def calcular_imc(peso, altura):
    """Calcula o IMC: peso (kg) dividido pela altura (m) ao quadrado."""
    return peso / (altura ** 2)

def calcular_idade(nascimento):
    """Calcula a idade aproximada em anos a partir da data de nascimento."""
    from datetime import date
    hoje = date.today()
    idade = (hoje - nascimento).days // 365
    return idade


for ano in (2002, 1950, 2023, 2025):
    print(ano, "é bissexto?", e_bissexto(ano))

print("IMC de 70 kg e 1,75 m:", round(calcular_imc(70, 1.75), 1))
print("IMC de 90 kg e 1,80 m:", round(calcular_imc(90, 1.80), 1))
print("calcular_idade", calcular_idade(0, 5, 15)), "anos")