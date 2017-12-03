import pymysql
import datetime

current_time = str(datetime.datetime.now().time())

host = 'localhost'
database = 'RetroPie'
user = 'root'

# connects to the database
conn = pymysql.connect(host=host, user=user, db=database)
if conn:
    print('Connection to MySQL database', database, 'was successful!')

cursor = conn.cursor()

# mysql statement
sql_statement = 'INSERT INTO FinishedGameTimes VALUES (%s)'

# execution statement
cursor.execute(sql_statement, current_time)
conn.commit()

print('Bye!')
conn.close()
