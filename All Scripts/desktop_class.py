class Desktop:

    def __init__(self, storage : int, ram_memory : float, screen: float, model : str, 
                brand: str):
        
        try:
            self.__storage = storage
            self.__ram_memory = ram_memory
            self.__screen = screen
            self.__model = model
            self.__brand = brand

        except Exception:
            raise ValueError

    @property
    def storage(self):
        return self._storage
    
    @storage.setter
    def storage(self):
        if isinstance(self._storage, int):
            return self._storage
        else:
            raise TypeError

    @property
    def ram_memory(self):
        return self._ram_memory

    @ram_memory.setter
    def ram_memory(self):
        if isinstance(self._ram_memory, float):
            return self._ram_memory
        else:
            raise TypeError

    def change_ram_memory(self, new_ram_memory):
        if isinstance(new_ram_memory, float):
            self.__ram_memory = new_ram_memory
            print(colored('RAM Memory changed successfuly!', 'green'))
        else:
            raise TypeError

    def change_storage(self, new_storage):
        if isinstance(new_storage, int):
            self.__storage = new_storage
            print(colored('RAM Memory changed successfuly!', 'green'))
        else:
            raise TypeError

    def __str__(self):
        return f'''PC info:\nStorage: {self.__storage} GB
        \nRAM Memory:{self.__ram_memory} GB
        \nModel:{self.__model}
        \nBrand:{self.__brand}'''


if __name__ == "__main__":
    from time import sleep
    from colorama import init
    from termcolor import colored

    my_desktop = Desktop(512, 8, 19.6, "VivoBook", "Asus")
    other_desktop = Desktop(240, 10, 22.5, "Nitro i5", "Acer")
    my_desktop.change_storage(200)
    print(my_desktop)
    sleep(2.5)
    