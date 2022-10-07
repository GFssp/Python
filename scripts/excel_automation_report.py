import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'C:/Users/Guilh_000/Documents/Python_Basic/Python Avançado/datasets/Planilha de clientes atuais.xlsx'

df = pd.read_excel(excel_file_1)

df = df.drop(columns=['Unnamed: 0'])
df = df.drop(columns=['Unnamed: 1'])

print(df)
