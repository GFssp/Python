import itertools
import random
import time

numbers = list(range(1, 61))
dataset = sorted(itertools.combinations(numbers, 6))

def gen_sequences(dataset=None):
    if dataset == None:
        dataset = []
    else:
        for sequence in dataset:
            yield sequence

result = gen_sequences(dataset)
for s in result:
    print(s)
