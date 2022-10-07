import time
morse_dict = {'a': '.-', 
              'b': '-...', 
              'c':'-.-.', 
              'd': '-..',
              'e': '.',
              'f': '..-.',
              'g': '--.',
              'h': '....',
              'i': '..',
              'j': '.---',
              'k': '-.-.',
              'l': '.-..',
              'm': '--',
              'n': '-.',
              'o': '---',
              'p': '.--.',
              'q': '--.-',
              'r': '.-.',
              's': '...',
              't': '-',
              'u': '..-',
              'v': '...-',
              'w': '.--',
              'x': '-..-',
              'y': '-.--',
              'z': '--..',
              1 : '.----',
              2 : '..---',
              3 : '...--',
              4 : '....-',
              5 : '.....',
              6 : '-....',
              7 : '--...',
              8 : '---..',
              9 : '----.',
              0 : '-----'}

my_input = input("Digite algo: ")
print('Traduzindo para codigo morse...')
time.sleep(1.5)

if isinstance(my_input, str) or isinstance(my_input, int):
    result = []
    for letter in my_input:
        for l, code in morse_dict.items():
            if letter == l:
                result.append(code)
    print(result)

else:
    raise TypeError
    
time.sleep(2)

