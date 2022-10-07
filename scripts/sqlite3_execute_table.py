import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

c.execute(""" CREATE TABLE costumer (
        first_name text,
        last_name text
        email text)""")

c.execute("INSERT INTO customer VALUES ('John', 'Elder', 'john@code.com')")

# Commit our command
conn.commit()

# Close our connection
conn.close()
