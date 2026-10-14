import pandas as pd
notas = pd.Series([8.5, 6.0, 9.5, 5.0, 9.7], index=["Paulo", "Sergio", "Paula", "Marcos", "Mario"])
print(notas.mean(), notas.max())
