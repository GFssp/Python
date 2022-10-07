import sqlite3
from employee_class import employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {
                  'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


def line():
    print('-'*40)


line()
print('REGISTRO DE FUNCIONÁRIOS')
line()


while True:
    ask_nome = str(input('Nome: '))
    ask_sobrenome = str(input('Sobrenome: '))
    ask_sal = int(input('Salário: '))
    emp = employee(ask_nome, ask_sobrenome, ask_sal)
    insert_emp(emp)
    lista = []
    print('Funcionário adicionado com sucesso!')

    ask = str(input('Ver informações de registro? [S/N] ')).lower()
    if ask == 's':
        registro = get_emps_by_name(ask_sobrenome)
        lista.append(registro)
        print(registro)
    line()

    advice = str(input('Deseja continuar registros? [S/N]')).lower()
    if advice == 'n':
        print(lista)
        break
    else:
        line()
