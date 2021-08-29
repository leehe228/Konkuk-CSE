import pymysql

conn = pymysql.connect( host='localhost', user='db2020', password='db2020', db='university')

curs = conn.cursor(pymysql.cursors.DictCursor)

SNO = 6000
sql = 'delete from student where sno=%d' % (SNO)

curs.execute(sql)
conn.commit()

curs.close()
conn.close()

print('done')
