# Se você deseja que os valores sejam adicionados e acumulados em uma lista, essa função é melhor
def add_names_to_alist(names, agg_list=[]):
    for name in names:
        aggregate_list.append(name)
    return aggregate_list


# Caso deseja adicionar valores a uma lista que não se acumula e reinicia a cada vez usada
def add_names_to_list(names, agg_list=None):
    if isinstance(agg_list, type(None)):
        agg_list = []
    for name in names:
        agg_list.append(name)
    return agg_list
