import collections

# Version 1
def check_duplicate(my_string):
    repetition = []
    if isinstance(my_string, str):
        for letter in my_string:
            result = my_string.count(letter)
            repetition.append(result)
        if 2 in repetition:
            return True    
        else:
            return False
    else:
        raise TypeError

# Version 2
def check_duplicate2(my_string):
    if isinstance(my_string, str):
        for letter in my_string:
            yield my_string.count(letter)
    else:
        raise TypeError

repet_list = []
for r in check_duplicate2('como vai'):
    repet_list.append(r)
if 2 in repet_list:
    print(True)
else:
    print(False)

# Version 3
def check_duplicate3(my_string):
    if isinstance(my_string, str):
        repetitions = collections.Counter(my_string).most_common(2)
        return repetitions

result = check_duplicate3("ola como vai")
print(result)




