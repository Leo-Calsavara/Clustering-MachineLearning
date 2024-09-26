import csv

# Dicionário para mapear os valores a serem alterados
substituicoes = {
    'A61': '1', 'A62': '2', 'A63': '3', 'A64': '4', 'A65': '5',
    'A71': '1', 'A72': '2', 'A73': '3', 'A74': '4', 'A75': '5',
    'A91': '1', 'A92': '2', 'A93': '3', 'A94': '4', 'A95': '5',
    'A101': '1', 'A102': '2', 'A103': '3',
    'A201': '1', 'A202': '2', 'A191': '1', 'A192': '2',
    'A171': '1', 'A172': '2', 'A173': '3', 'A174': '4',
    'A151': '1', 'A152': '2', 'A153': '3',
    'A141': '1', 'A142': '2', 'A143': '3'
}

# Caminho para o arquivo CSV de entrada e saída
input_file = 'arquivo.csv'
output_file = 'arquivo_modificado.csv'

# Leitura do arquivo CSV e modificação dos valores
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    linhas = list(reader)

# Abre o arquivo CSV para escrita e aplica as substituições
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Para cada linha no CSV
    for linha in linhas:
        # Substitui os valores da linha de acordo com o dicionário
        linha_modificada = [substituicoes.get(valor, valor) for valor in linha]
        # Escreve a linha modificada no novo arquivo CSV
        writer.writerow(linha_modificada)

print(f"Arquivo {output_file} criado com as substituições.")
