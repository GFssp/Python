import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
cursor = conn.cursor()

# Create a Table
cursor.execute("""CREATE TABLE customers (

    first_name text,
    last_name text,
    email text
    )""")


# Commit our command
conn.commit()

# Close our connection
conn.close()
