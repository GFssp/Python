import time

with open('names.txt', 'r+') as f:
    names = f.readlines()[:1000000]
    names_set = set(names)


def in_names():
    ret = []
    for i in range(100):
        ret.append(str(i) in names)
    return ret


def in_names_set():
    ret = []
    for i in range(100):
        ret.append(str(i) in names_set)
    return ret


print('Runnning in_names')
s = time.time()
in_names()
print('Time taken:', time.time() - s)

print('Runnning in_names_set')
s = time.time()
in_names_set()
print('Time taken:', time.time() - s)
