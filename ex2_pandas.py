import pandas as pd
dados = {
        "titulo": ["Homem Aranha",
                    "Batman",
                    "Mortal Kombat",
                    "suspense",
                    "Ação"],
        "Ano": [2004, 2006, 2020, 2011, 2014],
        "nota": [8.5, 6.0, 9.5, 5.0, 9.7]
        }
mini = pd.DataFrame(dados)
print(mini["titulo"])
print(mini[["Ano", "nota"]])
print(mini["Ano"].dtype, mini["nota"].dtype)