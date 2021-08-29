import pymysql

conn = pymysql.connect( host='localhost', user='db2020', password='db2020', db='university')

# curs = conn.cursor()
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from student'
curs.execute(sql)

#rows = curs.fetchall()
#print(rows)

row = curs.fetchone()

while row:
    print('학번 : %d, 이름 : %s' %(row['SNO'], row['SNAME']))
    row = curs.fetchone()

curs.close()
conn.close()

print('done')
