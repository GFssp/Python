from time import sleep


def add_names_to_alist(data, agg_list=None, **info):

    for k, v in info.items():

        if isinstance(agg_list, type(None)):

            agg_list = []
            info[k] = agg_list
            agg_list.append(v)

        else:

            agg_list = []
            info[k] = agg_list
            agg_list.append(v)

    return info


lista = ['Guilherme', 19, 1.78]
print(add_names_to_alist(lista, Name=lista[0], Age=lista[1], Heigth=lista[2]))
sleep(2)
