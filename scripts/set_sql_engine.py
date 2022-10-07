import pandas as pd
import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:gui2002@localhost:3306/sql-database')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbdir/employees.db'


df = pd.read_sql_table('employees.db', engine)
