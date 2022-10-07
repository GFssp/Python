import openpyxl
import time

wb = openpyxl.load_workbook('Cópia de Base Vendas.xlsx')
sheet = wb['BaseVendas']

for s in sheet.iter_rows(values_only=True):
    print(s)
time.sleep(10)
