import os
import pandas as pd
from tqdm import tqdm

# Pasta que contém as planilhas a serem combinadas
pasta = 'Planihas'

# Lista de nomes de arquivos na pasta
arquivos = [os.path.join(pasta, arquivo) for arquivo in os.listdir(pasta) if arquivo.endswith('.xlsx')]

# Criar uma lista para armazenar os DataFrames das planilhas
dataframes = []

# Loop através dos arquivos e leia-os em DataFrames
for arquivo in tqdm(arquivos, desc="Lendo Planilhas"):
    df = pd.read_excel(arquivo)
    dataframes.append(df)

# Combine os DataFrames em um único DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Salve o DataFrame combinado em um novo arquivo
combined_df.to_excel('planilha_combinada.xlsx', index=False)

print("Planilhas combinadas com sucesso!")