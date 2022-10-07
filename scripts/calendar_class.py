class Calendar:

    def __init__(self):
        pass
        
    def incluir(self, nome, telefone, email):

        cont = 0
        self.nome = nome
        self.tel = telefone
        self.email = email

        while cont < 10:

            lista = []
            lista.append(self.nome)
            lista.append(self.tel)
            lista.append(self.email)
            cont += 1
        
        lista_geral.append(lista)
        print('Contato Incluído com Sucesso!')

    def remover(self, nome, telefone, email):

        self.nome = nome
        self.tel = telefone
        self.email = email

        for contato in lista_geral:
            
            if contato in lista_geral:
                lista_geral.remove(contato)
                print('Contato Excluído com Sucesso!')
            else:
                print('Contato Inexistente')

    def buscar(self, nome, telefone, **email):

        self.nome = nome
        self.tel = telefone
        self.email = email

        for contado in lista_geral:
            
            if contado in lista_geral:
                print(contado)

            else:
                print('Contaton Inexistente')

    def listar(self):

        print(lista_geral)

lista_geral = []
    
Calendar().incluir('Guilherme', '87947383', 'guilherme@gmail.com')
Calendar().incluir('José', '3453453', 'jose@gmail.com')
Calendar().remover('Guilherme', '87947383', 'guilherme@gmail.com')
Calendar().buscar('José', '3453453')
Calendar().listar()




