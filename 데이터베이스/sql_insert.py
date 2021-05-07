import pymysql

conn = pymysql.connect( host='localhost', user='db2020', password='db2020', db='university')

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = 'insert into student(SNO, SNAME, DEPT) values (%s, %s, %s)'
a = (6000, '김동일', '컴퓨터')
b = (7000, '박수용', '전자')
c = (8000, '장용성', '산공')

st_list = [a, b, c]

# curs.execute(sql, a)
curs.executemany(sql, st_list)
conn.commit()

curs.close()
conn.close()

print('done')
