import pymysql

conn = pymysql.connect( host='localhost', user='db2020', password='db2020', db='university')

curs = conn.cursor(pymysql.cursors.DictCursor)

SNO = 7000
DEPT = '컴퓨터'
sql = "update student set DEPT='%s' where sno='%d'" % (DEPT, SNO)

curs.execute(sql)
conn.commit()

curs.close()
conn.close()

print('done')
