import pandas as pd


# Lendo a base de dados do Excel para um DataFrame
df = pd.read_excel('dados.xlsx')


print(df)
print("\n\n")
print("Media de idade:", df['Idade'].mean())
print("Idade Mínima:", df['Idade'].min())
print("Idade Máxima:", df['Idade'].max())
print("\n\n")
pessoas_acima_de_30 = df[df['Idade'] > 30]
pessoas_abaixo_de_30 = df[df["Idade"] < 30]
print(f"Pessoas com idade superior a 30 anos: {pessoas_acima_de_30}")
print("\n\n")
print(f"Pessoas com idade superior a 30 anos: {pessoas_abaixo_de_30}")

