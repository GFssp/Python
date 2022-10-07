from time import sleep

class Televisor:

    def __init__(self, fabricante, modelo, canal_atual, lista_canais, volume):

        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_canais = lista_canais
        self.volume = volume

        self.lista_canais = []

    def aumentar_volume(self):

        if self.volume < 99:
            self.volume += 1
            print('Canal aumentado para', self.volume)

        else:
            print('Não é possível aumentar de canal')
        
    def diminuir_volume(self):

        if self.volume > 1:
            self.volume -= 1
            print('Canal diminuído para', self.volume)

        else:
            print('Não é possível diminuir de canal')

    def sintonizar_canal(self, novo_canal):
        
        self.lista_canais.append(novo_canal)
        print('Canal', novo_canal, 'sintonizado com sucesso!')

    def trocar_canal(self):

        p = int(input('Qual canal deseja botar? '))
        if p not in self.lista_canais:
            adv = input('O canal digitado não está na lista dos canais sincronizados, deseja sintoniza-lo? ').lower()
            if adv == 'sim':
                Televisor.sintonizar_canal(p)
            else:
                print('Canal Indisponível')
        else:
            print('Canal Atual:', self.canal_atual)


tv = Televisor('Samsung', 'Smart 55', 15, [], 45)
