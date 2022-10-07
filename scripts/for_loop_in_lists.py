import csv

tabela = [['Aluno', 'Nota 1', 'Nota 2', 'Presenças'],
          ['Luke', 7, 9, 15],
          ['Han', 4, 7, 10],
          ['Leia', 9, 9, 16]]

print('Imprimindo cada elemento individual da tabela:')
for linha in tabela:
    for elemento in linha:
        print(elemento)

print('Imprimindo cada "linha" da tabela:')
for linha in tabela:
    print(linha)

print('Imprimindo o elemento na linha 2, coluna 0:')
print(tabela[2][0])
