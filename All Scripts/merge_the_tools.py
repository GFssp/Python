from collections import Counter

def merge_the_tools(string, k):
    chunks = list(zip(*[iter(string)] * k))
    for group in chunks:
        # IMPORTANTE - AGRUPAMENTO DE ELEMENTOS E REMOÇÃO DE DUPLICATAS
        group = dict.fromkeys(group)
        print("".join(group))
        
        
if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)