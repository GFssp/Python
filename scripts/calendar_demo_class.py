from time import sleep

class incluir:
    
    def __init__(self, nome, telefone, email):
        
        cont = 0
        self.nome = nome
        self.telefone = telefone
        self.email = email
            
        while cont < 10:
            
            lista = []
            lista.append(self.nome)
            lista.append(self.telefone)
            lista.append(self.email)
            cont += 1
        
        lista_geral.append(lista)
        print('Contado Adicionado com Sucesso!')    
        
class remover:
    
    def __init__(self, nome, telefone, email):
            
        self.nome = nome
        self.telefone = telefone
        self.email = email

        for contato in lista_geral:
            
            if contato in lista_geral:
                lista_geral.remove(contato)
                print('Contato Excluído com Sucesso!')
            else:
                print('Contato Inexistente')
                
class listar:
        
    def __init__(self):
        
        print('Lista de Contatos na Agenda Python:', end=' ')
        print(lista_geral)


lista_geral = [] 


incluir('Matheus', '9763647', 'Mat@gmail.com')
incluir('Gabriel', '8753627', 'Gab@gmail.com')

listar()
sleep(2)








