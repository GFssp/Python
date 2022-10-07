from collections import defaultdict

#Frequência de letras
string = "Guilherme"

d = defaultdict(int)
for c in string:
    d[c] += 1

print(d)