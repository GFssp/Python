from televisor import Televisor as tv

class ControleRemote():
    
    def __init__(self, televisão=tv):

        self.tv = televisão
        self.lista_canais = []

    def aumentar_volume(self):

        if tv.aumentar_volume() < 99:
            self.volume += 1
            print('Canal aumentado para', self.volume)

        else:
            print('Não é possível aumentar de canal')
        
    def diminuir_volume(self):

        if tv.diminuir_volume() > 1:
            tv.diminuir_volume() -= 1
            print('Canal diminuído para', tv.diminuir_volume())

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
            print('Canal Atual:', tv.sintonizar_canal())








