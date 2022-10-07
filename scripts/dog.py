class Dog:

    def __init__(self, cor_do_pelo, altura, cor_do_olho, velocidade):
        self.cor_do_pelo = cor_do_pelo
        self.altura = altura
        self.cor_do_olho = cor_do_olho
        self.velocidade = velocidade

    def registrar(self, nome, data_nascimento, peso):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.peso = peso

def listar(*dogs_info):

    lista = []
    lista.append(dogs_info)

    print(lista)
    
def main():

    print('REGISTRO DE CÃES!')
    running = True

    while running:

        try:

            cor_do_pelo = str(input('Cor do Pelo: '))
            altura = float(input('Altura: '))
            cor_do_olho = str(input('Cor dos olhos: '))
            velocidade = float(input('Velocidade: '))

            dog = Dog(cor_do_pelo, altura, cor_do_olho, velocidade)

            nome = str(input('Nome: '))
            data_nacimento = input('Data de Nascimento: ')
            peso = float(input('Peso: '))

            dog.registrar(nome, data_nacimento, peso)

        except Exception as E:

            print(f'Erro: {E}')

        try:

            ask = str(input('Deseja Cadastrar outro cão: '))
        
        except Exception as E1:

            print(f'Erro: {E1}')
        
        if 'n'.lower() in ask[0]:

            listar(dog.__dict__)

        if 's'.lower() not in ask[0]:

            print('Erro.')
            break


if __name__=='__main__':
    import time
    time.sleep(1.5)
    main()