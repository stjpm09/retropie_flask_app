import sys
import pymysql
import datetime

game_name = ""

for word in sys.argv:
        game_name = game_name + word

game_name_list = game_name.split('/')
game_name = game_name_list[len(game_name_list)-1]
game_name_list = game_name.split('.')
game_name = game_name_list[0]

#game_name = sys.argv[2]
system_name = sys.argv[1]
system_list = system_name.split('/')
current_time = str(datetime.datetime.now().time())

system_name = str(system_list[5])

print('game_name:', game_name)
print('system_name:', system_name)
print('current_time:', current_time)

host = 'localhost'
database = 'RetroPie'
user = 'root'

# connects to the database
conn = pymysql.connect(host=host, user=user, db=database)
if conn:
    print('Connection to MySQL database', database, 'was successful!')

val = input('Enter')

cursor = conn.cursor()
cursor2 = conn.cursor()
# mysql statement
current_game_sql = 'INSERT INTO CurrentGame VALUES (%s, %s, %s)'

in_history_sql = 'SELECT game_name FROM GamesPlayed'

# execution statement
cursor.execute(current_game_sql, (game_name, system_name, current_time))

conn.commit()

cursor2.execute(in_history_sql)
if game_name not in cursor2:
    game_history_sql = 'INSERT INTO GamesPlayed VALUES (%s, %s)'
    cursor.execute(game_history_sql, (game_name, system_name))
    conn.commit()

print('Bye!')
conn.close()



