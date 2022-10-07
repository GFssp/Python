import math
import argparse

# Acesse código pelo prompt
# Descrição: matavar torna as informações mais 'limpas' no prompt
# A função da variavel group deve ocorrer caso só os radianos ou só a altura seja mostrada
parser = argparse.ArgumentParser(description='Calculate volume of a Cylinter')
parser.add_argument('-r', '--radius', type=int,
                    metavar='', required=True, help='Radius of Cylinter')
parser.add_argument('-H', '--heigth', type=int,
                    metavar='', required=True, help='Heigth of Cylinter')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet',
                   action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print quiet')
args = parser.parse_args()


def cylinder_volume(radius, heigth):

    vol = (math.pi) * (radius ** 2) * (heigth)
    return vol

#hey
# Exemplo de código a ser digitado no prompt para acessar o programa: python argparser_demo.py -r 4 -H 4 - v


if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.heigth)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(
            f'Volume of a cylinder with radius {args.radius} and heigth {args.heigth} is {volume}')
    else:
        print(f'Volume of Cylinder = {volume}')
