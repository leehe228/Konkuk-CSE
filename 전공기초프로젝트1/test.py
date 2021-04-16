from dnn import (Model_Time, Model_Week)
import numpy as np

model_time = Model_Time()
model_week = Model_Week()

EXP_SET = [['할일1', 0, 15, 0, 1, 30, ['월', '수'], '내용1'], ['할일2', 1, 9, 0, 1, 0, ['목', '금'], '내용2'], ['할일3', 0, 19, 30, 2, 30, ['토', '일'], '내용3']]

task = ['할일4', 0, 15, 0, 1, 30, ['월', '수'], '내용4']

tempTag = [0, 0, 0]
tempTag[task[1]] = 1
p_data = np.array([tempTag])

if len(EXP_SET) == 0:
    x_data = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    y_time_data = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]])
    y_week_data = np.array([[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0]])
else:
    l_tag = list()
    l_time = list()
    l_week = list()

    for exp in EXP_SET:
        tempTag = [0, 0, 0]
        tempTime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tempWeek = [0, 0, 0, 0, 0, 0, 0]
        hw = ['월', '화', '수', '목', '금', '토', '일']
        tempTag[exp[1]] = 1
        l_tag.append(tempTag)
        tempTime[exp[2] - 9] = 1
        l_time.append(tempTime)
        tempWeek[hw.index(exp[6][0])] = 1
        l_week.append(tempWeek)

    x_data = np.array(l_tag)
    y_time_data = np.array(l_time)
    y_week_data = np.array(l_week)


print('x_data :', x_data)
print('y_time_data :', y_time_data)
print('y_week_data :', y_week_data)
print('p_data :', p_data)

t1 = model_time.PREDICT(x_data, y_time_data, p_data)
t2 = model_week.PREDICT(x_data, y_week_data, p_data)