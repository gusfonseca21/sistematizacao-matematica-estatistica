"Código para o cálculo e transformação dos dados para a matéria de Matemática e Estatística para Programação"

import pandas as pd

dataframe = pd.read_excel('Sistematização.xlsx')

### ! IDADE
# media_ar_idade = dataframe["Idade"].mean()

# mediana_idade = dataframe["Idade"].median()

# moda_idade = dataframe["Idade"].mode()

# variancia_idade = dataframe["Idade"].var()

# desvio_padrao_idade = dataframe["Idade"].std()

# quantile_idade = dataframe["Idade"].quantile([0.25, 0.5, 0.75])

# # print("Idade")
# print("Média Aritmética: ", media_ar_idade)
# print("Mediana: ", mediana_idade)
# print("Moda: ", moda_idade)
# print("Variância: ", variancia_idade)
# print("Desvio Padrão: ", desvio_padrao_idade)
# print("Quantile: ", quantile_idade)

# # Cabeçalho


# idade_unique = dataframe["Idade"].unique()
# Xi_idade = pd.Series(idade_unique).sort_values().values

# total_rows_idade = len(dataframe["Idade"])

# # Os últimos valores de fac e Fac são o Total

# data_idade = []
# fi_idade = []
# fac_idade = []
# fad_idade = []
# Fi_idade = []
# Fac_idade = []
# Fad_idade = []

# # Calculando array de ocorrências (fi_idade)
# for unique_age in Xi_idade:
#     counter = 0
#     for age_val in dataframe["Idade"]:
#         if age_val == unique_age:
#             counter += 1
#     fi_idade.append(counter)
#     Fi_idade.append(counter / total_rows_idade * 100)

# # Calculando frequência ascendente (fac_idade)
# for i, num_occurrences in enumerate(fi_idade):
#     if i == 0:
#         fac_idade.append(num_occurrences)
#         Fac_idade.append(num_occurrences / total_rows_idade * 100)
#     if 0 < i < len(fi_idade):
#         value = fac_idade[i - 1] + fi_idade[i]
#         fac_idade.append(value)
#         Fac_idade.append(round(value / total_rows_idade * 100, 1))

# # Calculando frequência descendente (fad_idade)
# for i, num_occurrences in enumerate(sorted(fi_idade, reverse=True)):
#     if i == 0:
#         fad_idade.append(total_rows_idade)
#         Fad_idade.append(total_rows_idade / total_rows_idade * 100)
#     if 0 < i <= len(fi_idade):
#         value = fad_idade[i - 1] - fi_idade[i - 1]
#         fad_idade.append(value)
#         Fad_idade.append(round(value / total_rows_idade * 100, 1))

# # print("fi_idade: ", fi_idade)
# # print("Fi_idade: ", Fi_idade)
# # print("fac_idade: ", fac_idade)
# # print("Fac_idade: ", Fac_idade)
# # print("Fad_idade: ", Fad_idade)

# for i, num_occurrences in enumerate(Xi_idade):
#     data_idade.append([num_occurrences, fi_idade[i], fac_idade[i], fad_idade[i], f"{Fi_idade[i]}%", f"{Fac_idade[i]}%", f"{Fad_idade[i]}%"])

# # Última linha, totais para fi_idade e Fi_idade
# data_idade.append(["Total:", total_rows_idade, "", "", "100%", "", ""])

# df = pd.DataFrame(data_idade, columns=cols)

# # print(df)

# df.to_excel('output.xlsx', index_label="Index")

### ! GÊNERO
# male_counter = 0
# female_counter = 0
# for gender in dataframe["Gênero"]:
#     if gender == "Masculino":
#         male_counter += 1
#     if gender == "Feminino":
#         female_counter += 1
# print("Número de homens: ", male_counter)
# print("Número de mulheres: ", female_counter)

def generate_table (col_name):
    unique_values = dataframe[col_name].unique()
    Xi = pd.Series(unique_values).sort_values().values
    total = len(dataframe[col_name])

    fi = []
    fac = []
    fad = []
    Fi = []
    Fac = []
    Fad = []

    data = []

    #* Calculando fi e Fi
    for unique_value in Xi:
        counter = 0
        for value in dataframe[col_name]:
            if value == unique_value:
                counter += 1
        fi.append(counter)
        Fi.append(counter / total * 100)

    #* Calculando fac e Fac
    for i, num_occurrences in enumerate(fi):
        if i == 0:
            fac.append(num_occurrences)
            Fac.append(num_occurrences / total * 100)
        if 0 < i < len(fi):
            value = fac[i - 1] + fi[i]
            fac.append(value)
            Fac.append(round(value / total * 100, 1))

    #* Calculando fad e Fad
    for i, num_occurrences in enumerate(sorted(fi, reverse=True)):
        if i == 0:
            fad.append(total)
            Fad.append(total / total * 100)
        if 0 < i <= len(fi):
            value = fad[i - 1] - fi[i - 1]
            fad.append(value)
            Fad.append(round(value / total * 100, 1))

    #* Dados estatísticos básicos
    media = dataframe[col_name].mean()
    moda = dataframe[col_name].mode()
    mediana = dataframe[col_name].median()
    desvio_padrao = dataframe[col_name].std()

    #* Gerando as linhas da tabela
    for i, num_occurrences in enumerate(Xi):
        data.append([num_occurrences, fi[i], fac[i], fad[i], f"{Fi[i]}%", f"{Fac[i]}%", f"{Fad[i]}%"])

    data.append(["Total:", total, "", "", "100%", "", ""])

    data.append([f"Média: {media}", f"Moda: {moda}", f"Mediana: {mediana}", f"Desvio Padrão: {desvio_padrao}"])

    #* Gerando a tabela

    # Cabeçalho
    cols = pd.MultiIndex.from_tuples([("", "Xi"), ("Frequência absoluta", "fi"), ("Frequência absoluta", "fac"), ("Frequência absoluta", "fad"), ("Frequência relativa", "Fi"), ("Frequência relativa", "Fac"), ("Frequência relativa", "Fad")])

    df = pd.DataFrame(data, columns=cols)

    # print(df)

    df.to_excel(f"{col_name}.xlsx", index_label="Linha")

generate_table("Nível de satisfação com o trabalho atual")

