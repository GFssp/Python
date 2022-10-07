import logging

logging.basicConfig(filename='Employees.log', level=logging.INFO,
                    format='%(levelname)s:%(name)s:%(message)s')

class Employee:

    def __init__(self, first, last):

        self.first = first
        self.last = last

        logging.info(
            'Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


def line():
    print('-'*40)


line()
print('REGISTRAR USUÁRIO')
line()

name = str(input('Nome: '))
sobrenome = str(input('Sobrenome: '))
print('Employee Registered Successfully!')

Employee(name, sobrenome)
