from time import time

class Cronômetro:

    def __init__(self, tempo):

        self.t = tempo
        self.t = time.sleep(tempo)

    def __repr__(self):

        return f'Return {self.t}'


