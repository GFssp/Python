from itertools import accumulate

def accumulation(elements):
    running_sum = accumulate(elements)
    print(list(running_sum))

accumulation([1, 2, 3, 4])
