"Código para o cálculo e transformação dos dados para a matéria de Matemática e Estatística para Programação"

import pandas as pd

dataframe = pd.read_excel('Sistematização.xlsx')

# IDADE
media_ar_idade = dataframe["Idade"].mean()

mediana_idade = dataframe["Idade"].median()

moda_idade = dataframe["Idade"].mode()

variancia_idade = dataframe["Idade"].var()

desvio_padrao_idade = dataframe["Idade"].std()

quantile_idade = dataframe["Idade"].quantile([0.25, 0.5, 0.75])

# print("Idade")
# print("Média Aritmética: ", media_ar_idade)
# print("Mediana: ", mediana_idade)
# print("Moda: ", moda_idade)
# print("Variância: ", variancia_idade)
# print("Desvio Padrão: ", desvio_padrao_idade)
# print("Quantile: ", quantile_idade)

# Cabeçalho
idade_cols = pd.MultiIndex.from_tuples([("", "Xi"), ("Frequência absoluta", "fi"), ("Frequência absoluta", "fac"), ("Frequência absoluta", "fad"), ("Frequência relativa", "Fi"), ("Frequência relativa", "Fac"), ("Frequência relativa", "Fad")])

idade_unique = dataframe["Idade"].unique()
Xi = pd.Series(idade_unique).sort_values().values


col_num = len(Xi)
total_rows_idade = len(dataframe["Idade"])

# Os últimos valores de fac e Fac são o Total

data = []
fi = []
fac = []
fad = []
Fi = []
Fac = []
Fad = []

# Calculando array de ocorrências (fi)
for unique_age in Xi:
    counter = 0
    for age_val in dataframe["Idade"]:
        if age_val == unique_age:
            counter += 1
    fi.append(counter)
    Fi.append(counter / total_rows_idade * 100)

# Calculando frequência ascendente (fac)
for i, num_occurrences in enumerate(fi):
    if i == 0:
        fac.append(num_occurrences)
        Fac.append(num_occurrences / total_rows_idade * 100)
    if 0 < i < len(fi):
        value = fac[i - 1] + fi[i]
        fac.append(value)
        Fac.append(round(value / total_rows_idade * 100, 1))

# Calculando frequência descendente (fad)
for i, num_occurrences in enumerate(sorted(fi, reverse=True)):
    if i == 0:
        fad.append(total_rows_idade)
        Fad.append(total_rows_idade / total_rows_idade * 100)
    if 0 < i <= len(fi):
        value = fad[i - 1] - fi[i - 1]
        fad.append(value)
        Fad.append(round(value / total_rows_idade * 100, 1))

# print("fi: ", fi)
# print("Fi: ", Fi)
# print("fac: ", fac)
# print("Fac: ", Fac)
# print("Fad: ", Fad)

for i, num_occurrences in enumerate(Xi):
    data.append([num_occurrences, fi[i], fac[i], fad[i], f"{Fi[i]}%", f"{Fac[i]}%", f"{Fad[i]}%"])

# Última linha, totais para fi e Fi
data.append(["Total:", total_rows_idade, "", "", "100%", "", ""])

df = pd.DataFrame(data, columns=idade_cols)

# print(df)

df.to_excel('output.xlsx', index_label="Index")
