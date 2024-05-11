import pandas as pd
import openpyxl

# Leia o arquivo Parquet em um DataFrame
df = pd.read_parquet('bulletins.parquet')

wb = openpyxl.Workbook()
ws = wb.active

# Escreva o DataFrame na planilha
df.to_excel(ws)

# Salve o arquivo Excel
wb.save('meu_arquivo.xlsx')

