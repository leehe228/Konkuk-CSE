import pymysql

conn1 = pymysql.connect( host='localhost', user='db2020', password='db2020', db='university')
curs1 = conn1.cursor(pymysql.cursors.DictCursor)

conn2 = pymysql.connect( host='localhost', user='db2020', password='db2020', db='university')
curs2 = conn2.cursor(pymysql.cursors.DictCursor)

# Q. 컴퓨터과 학생들 중에서 2과목 이상 수강한 학생들의 기말고사 점수를 7점씩 올려라

# 1) 컴퓨터과 학생들 중에서 2과목 이상 수강한 학생들의 학번 검색
sql1 = """ select s.SNO
           from STUDENT s, ENROL e
           where s.SNO=e.SNO
           and s.DEPT='컴퓨터'
           group by e.SNO
           having count(*) >= 2 """

curs1.execute(sql1)
row = curs1.fetchone()

# 2) 해당 학생들이 수강한 ENROL에서 기말고사 점수를 7점씩 올려라
while row:
    sql2 = """ update ENROL
               set FINAL = FINAL + 7
               where SNO = %d""" % (row['SNO'])

    curs2.execute(sql2)
    conn2.commit()

    row = curs1.fetchone()


curs1.close()
conn1.close()

curs2.close()
conn2.close()

print('done')
