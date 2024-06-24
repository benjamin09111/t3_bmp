import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('./random_financial_data.xlsx')

# Guardar como CSV
output_csv_file = './random_financial_data.csv'
df.to_csv(output_csv_file, index=False)




