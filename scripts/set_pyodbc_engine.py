import set_pyodbc_engine

# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'server_name'
database = ('Mydb', 'port')
username = 'myusername'

cnxn = set_pyodbc_engine
cursor = cnxn.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username)
