import pandas as pd
sujo = pd.read_csv("Exercicio aula1/Exercicio lista/sujo.csv")
print(sujo.shape)
print(sujo.isna().sum())