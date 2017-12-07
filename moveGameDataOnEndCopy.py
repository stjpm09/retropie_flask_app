import pymysql

host = 'localhost'
database = 'RetroPie'
user = 'root'

# connects to the database
conn = pymysql.connect(host=host, user=user, db=database)

cursor = conn.cursor()

# mysql statement
sql_statement = 'DELETE FROM CurrentGame'

# execution statement
cursor.execute(sql_statement)
conn.commit()

print('Bye!')
conn.close()
