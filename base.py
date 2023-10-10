import pandas as pd

dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25,30,35,40],
    'Cidade': ['Nova York', 'Londres', 'Paris', 'Berlim']
}

df = pd.DataFrame(dados)

df.to_excel('dados.xlsx', index=False)

print("Dados salvos com sucesso em dados.xlsx")