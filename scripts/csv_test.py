import csv

tabela = [['Aluno', 'Nota 1', 'Nota 2', 'Presenças'],
          ['Luke', 7, 9, 15],
          ['Han', 4, 7, 10],
          ['Leia', 9, 9, 16]]

# cria o arquivo CSV
arquivo = open('personagens.csv', 'w')

# definindo as regras do nosso CSV:
# ele será escrito no arquivo apontado pela variável 'arquivo'
# seus elementos serão delimitados (delimiter) pelo símbolo ';'
# suas linhas serão encerradas (lineterminator) por uma quebra de linha
escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')

# escreve uma lista de listas em formato CSV:
escritor.writerows(tabela)

arquivo.close()
