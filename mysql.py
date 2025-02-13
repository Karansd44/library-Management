import mysql.connector as sql
cnx = sql.connect(
    user='root', password='karan123', host='127.0.0.1',
    database='sys'
)
cursor=cnx.cursor()
cursor.execute('select * from`sys_config`;')
data = cursor.fetchall()
for d in data:
    print(data)
cnx.close()