class Planeta:

    def __init__(self, diametro, area, gravidade):

        self.diametro = diametro
        self.area = area
        self.gravidade = gravidade


    def __str__(self):
        return f'Diâmetro da terra: {self.diametro} Km\nArea da superfície: {self.area} x 10³ Km\nValor da gravidade: {self.gravidade} m/s²'


class Continente(Planeta):

    def __init__(self,nome, qt_paises, area, populacao):

        self.nome = nome
        self.qt_paises = qt_paises
        self.area = area
        self.populacao = populacao
    

class Pais(Continente):

    def __init__(self, lingua, continente, maior_cidade):

        self.lingua = lingua
        self.continente = continente
        self.maior_cidade = maior_cidade

    
terra = Planeta(12.742, 150100, 10)

america = Continente('América', 35, 42550, 1_000_000_000)
africa = Continente('África', 54, 30370, 1_216_000_000)
asia = Continente('Ásia', 50, 44_580_580, 4_561_000_000)
europa = Continente('Europa', 50, 17075.4, 746_400_000)
oceania = Continente('Oceania', 14, 9_008_458, 40_117_432)

brasil = Pais('Português', america.nome, 'São Paulo')
print(brasil.__dict__)
        

    
        


        

