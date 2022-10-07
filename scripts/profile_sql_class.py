class Profiles2():

    def __init__(self, dataList=[]):

        init()
        print(colored('Hey, Welcome!', 'green'))
        self.dataList = dataList

    def get_data(self):

        def has_numbers(input_text):
            condition = any(char.isdigit() for char in input_text)

            return condition

        self.name = str(input('Type a valid name to register: '))
        self.age = int(input('Type a valid age to register: '))
        self.heigth = float(input('Type a valid heigth to register: '))
        self.weigth = float(input('Type a valid weigth to register: '))

        if has_numbers(self.name):
            raise TypeError(colored('INVALID NAME', 'red'))
            sleep(2)

        self.dataList.append(self.name)
        self.dataList.append(self.age)
        self.dataList.append(self.heigth)
        self.dataList.append(self.weigth)

        return self.dataList


def get_structure(data, agg_list=None, **pdict):

    for k, v in pdict.items():

        if isinstance(agg_list, type(None)):

            agg_list = []
            pdict[k] = agg_list
            agg_list.append(v)

        else:

            agg_list = []
            pdict[k] = agg_list
            agg_list.append(v)

    return pdict


def main():

    running = True
    while running:

        rawData = Profiles2([]).get_data()

        data = get_structure([], rawData, Names=rawData[0],
                             Ages=rawData[1],
                             Heigth=rawData[2],
                             Weigth=rawData[3])

        rProfile = json.dumps(data)
        logging.debug(rProfile)
        print(rProfile)

        ask = input('Continue?[Y/N] ').lower()
        if 'n' in ask:
            break


if __name__ == '__main__':

    from colorama import init
    from termcolor import colored
    from time import sleep
    import json
    import logging

    logging.basicConfig(filename='Profiles.log', level=logging.DEBUG)

    main()
