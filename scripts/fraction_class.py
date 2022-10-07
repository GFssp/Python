class Fraction:

    def __init__(self, n, d):

        self.n = n
        self.d = d

    def __add__(self, other):

        if self.d > other.d:
            maior = self.d
        else:
            maior = other.d
        while True:
            if maior % self.d == 0 and maior % other.d == 0:
                print(f'MMC: {maior}')
                break
            else:
                maior += 1
        
        n1 = maior / self.d
        n2 = maior / other.d

        n3 = n1 * self.n
        n4 = n2 * other.n

        n5 = n4 + n3
        d = maior

        resultado = Fraction(n5, d)

        return resultado

    def __sub__(self, other):

        if self.d > other.d:
            maior = self.d
        else:
            maior = other.d
        while True:
            if maior % self.d == 0 and maior % other.d == 0:
                print(f'MMC: {maior}')
                break
            else:
                maior += 1
        
        n1 = maior / self.d
        n2 = maior / other.d

        n3 = n1 * self.n
        n4 = n2 * other.n

        n5 = n4 - n3
        d = maior

        resultado = Fraction(n5, d)

        return resultado

    def __mul__(self, other):

        novo_n = self.n * other.n
        novo_d = self.d * other.d

        resultado = Fraction(novo_n, novo_d)

        return resultado
    
    def __truediv__(self, other):

        novo_n = self.n * other.d
        novo_d = self.d * other.n

        resultado = Fraction(novo_n, novo_d)

        return resultado

    def __gt__(self, other):

        resultado1 = self.n / self.d
        resultado2 = other.n / other.d

        return resultado1 > resultado2

    def __ge__(self, other):

        resultado1 = self.n / self.d
        resultado2 = other.n / other.d

        return resultado1 >= resultado2

    def __lt__(self, other):

        resultado1 = self.n / self.d
        resultado2 = other.n / other.d

        return resultado1 < resultado2

    def __le__(self, other):

        resultado1 = self.n / self.d
        resultado2 = other.n / other.d

        return resultado1 <= resultado2

    def __eq__(self, other):

        resultado1 = self.n / self.d
        resultado2 = other.n / other.d

        return resultado1 == resultado2

    def __ne__(self, other):

        resultado1 = self.n / self.d
        resultado2 = other.n / other.d

        return resultado1 != resultado2

    def __repr__(self):

        return f'Fração ({self.n}, {self.d})'


f1 = Fraction(5, 12)
f2 = Fraction(8, 24)

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1 > f2)
