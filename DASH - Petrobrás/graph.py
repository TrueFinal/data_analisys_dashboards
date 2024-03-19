import pandas as pd

dados = 'dados_biodisel.csv'
df = pd.read_csv(dados, delimiter=',')
df = pd.DataFrame(df)

df['Mês/Ano'] = pd.to_datetime(df['Mês/Ano'].str.strip(), utc=False)
df['Ano'] = df['Mês/Ano'].dt.year
df['Vendas de Biodiesel'] = df['Vendas de Biodiesel'].str.replace(',', '').astype(float).astype(int)

df_agrupado = df.groupby(df['Ano']).agg({'Vendas de Biodiesel': 'sum'}).reset_index()

df_vendas_x_ano = pd.DataFrame(index=[0], columns=['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])

df = df.drop(df.columns[-1], axis=1)

for index, row in df_agrupado.iterrows():
    ano = str(row['Ano'])
    df_vendas_x_ano[ano] = row['Vendas de Biodiesel']