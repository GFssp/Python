class Client:

    def __init__(self, p_nome, u_nome, cod_cadastro, cpf):
        self.p_nome = p_nome
        self.u_nome = u_nome
        self.__cod_cadastro = cod_cadastro
        self.__cpf = cpf

    """ metodo 'email' passa a agir como atributo quando usado o método property """
    @property
    def email(self):
        return self.p_nome.lower() + "." + self.u_nome.lower() + "@mycompany.com"

    """ permite o uso da função print() no objeto da classe"""
    def __str__(self):
        return self.p_nome

    """ permite mostrar no terminal a representação do objeto da classe"""
    def __repr__(self) -> str:
        return self.email

    def __call__(self, client_dict_position):
        pass

    def __len__(self):
        return len(self.p_nome)


class Register:

    def __new__(cls, *args, **kwargs):
        return args, kwargs
    
    
a1 = Client("Guilherme", "Fernandes", '8375827', '52002300801')
c1 = Register(a1, company='TechExx')
print(c1)


