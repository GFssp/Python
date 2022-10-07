import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'John@code.com')")


conn.commit()

conn.close()



