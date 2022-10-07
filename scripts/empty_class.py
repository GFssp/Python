class Vazio:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __getattr__(self, atr_oculto):

        if atr_oculto == 'peso':
            return 70
        else:
            raise AttributeError(atr_oculto)
        
    def __getattribute__(self, __name: str) -> Any:
        pass

    def __setattr__(self, __name: str, __value: Any) -> None:
        pass
        
    
perfil = Vazio('Guilherme', 20)
print(perfil.peso)