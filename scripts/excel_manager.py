import openpyxl
import datetime

wb = openpyxl.load_workbook('Cópia de Base Vendas.xlsx')
sheet = wb['BaseVendas']

values = {}

for row in sheet.iter_rows(min_row=2, values_only=True):

    valuesID = row[0]
    value = {
        'Produto': row[1],
        'Quantidade Vendida': row[2],
        'Nome Completo': row[3],
        'Data da Venda': row[4],
        'Mês': row[5],
        'Loja': row[6],
        'Preço Unitário': row[7],
        'Faturamento na Venda': row[8]
    }

    values[valuesID] = value

