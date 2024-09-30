import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# 1. Carregar o arquivo CSV com o cabeçalho
# Suponha que o arquivo se chama 'dados.csv'
df = pd.read_csv('dados.csv')
# 2. Identificar as colunas numéricas que você deseja normalizar
numerical_cols = ['AT1', 'AT4', 'AT7', 'AT10', 'AT12', 'AT15', 'AT17']
# 3. Criar o scaler Min-Max para normalizar os dados
scaler = MinMaxScaler()
# 4. Aplicar o scaler apenas nas colunas numéricas
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
# 5. Salvar o DataFrame normalizado em um novo arquivo CSV
# O arquivo de saída será 'dados_normalizados.csv'
df.to_csv('dados_normalizados.csv', index=False)
print("Normalização concluída e os dados foram salvos em 'dados_normalizados.csv'")