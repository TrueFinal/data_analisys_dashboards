import numpy as np
import pandas as pd
import warnings

def data_tratamento(nome_arquivo, colunas, criar_dataframe=True, formato_data=None):
    try:
        # Verifica se a lista de colunas está vazia
        if not colunas:
            raise ValueError("A lista de colunas está vazia. Pelo menos uma coluna deve ser fornecida.")

        # Leitura do arquivo CSV
        df = pd.read_csv(nome_arquivo)

        # Verifica se as colunas especificadas existem no DataFrame
        for coluna in colunas:
            if coluna not in df.columns:
                raise ValueError(f"A coluna '{coluna}' não existe no arquivo de origem.")

        # Processa cada coluna
        for coluna in colunas:
            # Verifica se há valores NaN ou nulos na coluna
            nulos_trocados = df[coluna].isnull().sum()
            if nulos_trocados > 0:
                print(f"Foram encontrados {nulos_trocados} valores NaN ou nulos na coluna '{coluna}'. Substituindo por 0.")

            # Substitui NaN ou valores nulos por 0
            df[coluna].fillna(0, inplace=True)

            # Verifica o tipo de dados da coluna
            tipo_dados = df[coluna].dtype

            # Converte os valores da coluna para o formato de data especificado
            if tipo_dados == 'object' and formato_data:
                df[coluna] = pd.to_datetime(df[coluna], format=formato_data, errors='coerce')

            # Converte os valores da coluna para inteiros se forem floats
            elif np.issubdtype(tipo_dados, np.floating):
                df[coluna] = df[coluna].astype(int)

            # Caso contrário, retorna um erro
            elif tipo_dados != 'object':
                raise ValueError(f"O tipo de dados da coluna '{coluna}' não é suportado para conversão.")

            # Retorna o tipo de dados da coluna
            tipo_dados_atualizado = df[coluna].dtype

        # Retorna o DataFrame processado se criar_dataframe for True
        if criar_dataframe:
            return df
        else:
            return f"Os dados da coluna foram processados, mas o DataFrame não foi criado."

    except Exception as e:
        return f"Erro: {str(e)}"