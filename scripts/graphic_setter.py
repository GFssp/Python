import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Ler Arquivo csv
distribuicao_cloroquina = 'Dados de planilha para teste\DistribuicaoCloroquinaOseltamivir - DistribuicaoCloroquinaOseltamivir.csv'
df = pd.read_csv(distribuicao_cloroquina)

# Removendo linhas com regiões duplicadas e somando quantidade de lotes
df.drop('UF', inplace=True, axis=1)                                        # Retirando coluna de estados brasileiros
df = df.groupby(["REGIAO"], as_index=False)["QUANTIDADE"].sum()            # Agrupando regiões e somando quantidades

# Gerando estrutura do gráfico
fig, ax = plt.subplots(figsize=(10, 5))
df.plot(x='REGIAO', y='QUANTIDADE',kind='bar',alpha=0.75, rot=0, color='green', ax=ax)
plt.grid(True)
ax.set_title('Distribuição de Cloroquina no Brasil\n'
             '(Julho)')
ax.set_xlabel('(REGIÕES)')
ax.set_ylabel('QUANTIDADES DE LOTE (POR MILHÃO)')
plt.show()