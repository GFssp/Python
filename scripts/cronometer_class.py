from time import sleep

class Cronômetro:

    def __init__(self, tempo):

        sleep(tempo)

t = int(input('Até quanto tempo deseja cronometrar? (em segundos)'))
c = Cronômetro(t)
print(f'{t} segundos finalizados!')
sleep(2)


        


