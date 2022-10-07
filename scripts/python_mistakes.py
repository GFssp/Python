import time

# O código abaixo irá gerar um loop
# E também interpretará o comando pare (Ctrl C) como um erro (except) e vai dar a segunda mensagem
# while True:
#    try:
#        print("Wheeee! You can't stop me")
#        time.sleep(0.5)
#
#    except:
#        print('Oww... Whatever imma keep running')


# Nesse caso, o comando pare é interpretado de forma correta e o programa interrompe o loop
while True:
    try:
        print("Wheeee! You can't stop me")
        time.sleep(0.2)

    except Exception:
        print('Oww... Whatever imma keep running')
