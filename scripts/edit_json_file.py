import shelve

db = shelve.open('shelve.db')
db['Lista'] = [2, 6, 3, 6]
db = shelve.open('shelve.db', writeback=True)
db['Lista'].append(5)
print(db['Lista'])