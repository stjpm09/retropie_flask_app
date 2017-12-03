import sys
import pymysql
import datetime

game_name = sys.argv[2]
# system_name = sys.argv[1]
# system_list = system_name.split('/')
# current_time = str(datetime.datetime.now().time())

print('game_name:', game_name)
# print('system_name:', system_list[5])

val = input('Enter')

host = 'localhost'
database = 'RetroPie'
user = 'root'

# connects to the database
conn = pymysql.connect(host=host, user=user, db=database)
if conn:
    print('Connection to MySQL database', database, 'was successful!')

cursor = conn.cursor()

# mysql statement
sql_statement = 'INSERT INTO CurrentGame VALUES (%s)'

# execution statement
cursor.execute(sql_statement, game_name)
conn.commit()

print('Bye!')
conn.close()


