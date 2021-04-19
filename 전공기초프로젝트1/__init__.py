#-*-coding:utf-8-*-

import PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser, QMessageBox)
from PyQt5.QtGui import (QFontDatabase, QFont)
from PyQt5.QtCore import Qt

import sys
import subprocess
import numpy as np
from random import (randrange, random, choice)
import tensorflow as tf

# from dnn import (Model_Time, Model_Week)
# from text_datas import (TEXT_HELP, BAR, SPC, TEXT_TODO_HEADER, TEXT_TODO_CENTER, TEXT_TODO_BOTTOM, TEXT_TABLE, TEXT_MENU)

"""
# 전공기초프로젝트1 시간표 생성 프로그램
# 3239분반 4조
"""

# ========== 텍스트 데이터 ===========
TEXT_HELP = "명령어는 접두어 '/'와 명령단어를 공백 없이 붙여 사용한다.\n\
이 프로그램에서 사용할 수 있는 명령어는 다음과 같다.\n\
/도움말 명령어를 이용하면 이와 같이 도움말에 대한 정보를 열람할 수 있다.\n\
\n\
_________________________\n\
\n\
*시간표 명령어\n\
\n\
1. /이동 : 다음 목록의 페이지로 이동할 수 있다. 인자로 페이지 이름을 입력한다.\n\
페이지 목록 : 1) 메뉴페이지 2) 생성페이지 3) 결과페이지\n\
\n\
2. /입력완료 : 할 일을 모두 입력한 후 시간표를 생성하기 위해 사용한다. 인자는 없다.\n\
\n\
3. /저장 : 시간표와 할 일 데이터를 파일로 저장한다. 인자는 없다.\n\
\n\
4. /불러오기 : 시간표 혹은 할 일 데이터 파일을 열어 내용을 확인한다. 인자는 없다.\n\
\n\
_________________________\n\
\n\
*할 일 명령어\n\
\n\
1. /추가 : 할 일 데이터를 추가한다.\n\
필수로 입력하는 인자로 내용, 필수태그가 포함되어야 한다. \n\
내용은 접두, 접미어가 없고, 명령어 바로 뒤에 공백을 두고 입력되어야 한다. 필수 태그는 접두어로 샵(#)을 사용한다.\n\
선택 인자로 시작시각과 지속시간, 요일을 고정하거나, 서브 태그를 포함할 수 있다.\n\
시작시각, 지속시간, 요일은 모두 중괄호로 감싼다. 서브 태그는 접두어로 대시(-)를 사용한다. 서브 태그는 인자 중 가장 마지막에 입력되어야 한다.\n\
*예시 : /추가 친구만나기 #일과\n\
*예시 : /추가 물리문제 {금요일 수요일 13시} #과제 -p213부터 p238\n\
\n\
2. /검색 : 할 일을 검색한다. 인자로는 검색할 내용, 서브 태그 내용, 필수 태그 내용을 입력한다.\n\
인자로 검색어와 검색 조건을 입력한다. 접두어로는 대시(-)를 사용하며 몇 글자 이상 일치할 경우 출력할지 정수를 입력한다.\n\
검색할 내용은 명령어 바로 뒤에 공백을 두고 입력되어야 한다.\n\
*예시 : /검색 확통과제\n\
*예시 : /검색 미적분 과제 71 -3\n\
-> \"미적분과제71\" 텍스트 집합에서 3글자 이상 포함하는 결과를 출력한다.\n\
\n\
3. /수정 : 할 일을 수정한다. 인자로는 접두어 -와 수정할 구성요소 지칭어와 함께 올바른 접두, 접미어를 붙인 수정할 내용을 입력한다.\n\
*예시 : /수정 수학과제 -요일 {월요일}\n\
-> 요일의 경우 접두, 접미어로 중괄호를 사용하므로 중괄호를 사용한다.\n\
*예시 : /수정 영어과제 -태그 #일과\n\
-> 태그(필수 태그)의 경우 접두어로 샵(#)을 사용하므로 샵(#)을 사용한다.\n\
\n\
4. /삭제 : 할 일을 삭제한다. 인자로는 삭제할 할 일의 내용을 정확하게 입력한다.\n\
*예시 : /삭제 \"미적분수강\"\n\
-> 할 일의 내용이 정확히 일치해야 한다.\n\
\n\
_________________________\n\
\n\
*기타 명령어\n\
\n\
1. /종료 : 프로그램을 안전하게 종료합니다. 인자는 없다.\n"

BAR = "──────────"
SPC = "          "

TEXT_TODO_HEADER = "\
┌──────────┬──────────┬──────────┬──────────┬─────────────────────┬──────────┬────────────────────────┐\n\
│  할 일   │ 시작시각 │ 지속시간 │ 종료시각 │       요  일        │   태그   │        서브태그        │"

TEXT_TODO_CENTER = "\
├──────────┼──────────┼──────────┼──────────┼─────────────────────┼──────────┼────────────────────────┤\n\
│$T│$S│$R│$E│$W│$G│$D│"

TEXT_TODO_BOTTOM = "\
└──────────┴──────────┴──────────┴──────────┴─────────────────────┴──────────┴────────────────────────┘"

TEXT_TABLE = "\
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐\n\
│          │   MON    │   TUE    │   WED    │   THU    │   FRI    │   SAT    │   SUN    │\n\
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤\n\
│  09:00   │$M09│$T09│$W09│$H09│$F09│$S09│$U09│\n\
├──────────┼&M09┼&T09┼&W09┼&H09┼&F09┼&S09┼&U09┤\n\
│  10:00   │$M10│$T10│$W10│$H10│$F10│$S10│$U10│\n\
├──────────┼&M10┼&T10┼&W10┼&H10┼&F10┼&S10┼&U10┤\n\
│  11:00   │$M11│$T11│$W11│$H11│$F11│$S11│$U11│\n\
├──────────┼&M11┼&T11┼&W11┼&H11┼&F11┼&S11┼&U11┤\n\
│  12:00   │$M12│$T12│$W12│$H12│$F12│$S12│$U12│\n\
├──────────┼&M12┼&T12┼&W12┼&H12┼&F12┼&S12┼&U12┤\n\
│  13:00   │$M13│$T13│$W13│$H13│$F13│$S13│$U13│\n\
├──────────┼&M13┼&T13┼&W13┼&H13┼&F13┼&S13┼&U13┤\n\
│  14:00   │$M14│$T14│$W14│$H14│$F14│$S14│$U14│\n\
├──────────┼&M14┼&T14┼&W14┼&H14┼&F14┼&S14┼&U14┤\n\
│  15:00   │$M15│$T15│$W15│$H15│$F15│$S15│$U15│\n\
├──────────┼&M15┼&T15┼&W15┼&H15┼&F15┼&S15┼&U15┤\n\
│  16:00   │$M16│$T16│$W16│$H16│$F16│$S16│$U16│\n\
├──────────┼&M16┼&T16┼&W16┼&H16┼&F16┼&S16┼&U16┤\n\
│  17:00   │$M17│$T17│$W17│$H17│$F17│$S17│$U17│\n\
├──────────┼&M17┼&T17┼&W17┼&H17┼&F17┼&S17┼&U17┤\n\
│  18:00   │$M18│$T18│$W18│$H18│$F18│$S18│$U18│\n\
├──────────┼&M18┼&T18┼&W18┼&H18┼&F18┼&S18┼&U18┤\n\
│  19:00   │$M19│$T19│$W19│$H19│$F19│$S19│$U19│\n\
├──────────┼&M19┼&T19┼&W19┼&H19┼&F19┼&S19┼&U19┤\n\
│  20:00   │$M20│$T20│$W20│$H20│$F20│$S20│$U20│\n\
├──────────┼&M20┼&T20┼&W20┼&H20┼&F20┼&S20┼&U20┤\n\
│  21:00   │$M21│$T21│$W21│$H21│$F21│$S21│$U21│\n\
├──────────┼&M21┼&T21┼&W21┼&H21┼&F21┼&S21┼&U21┤\n\
│  22:00   │$M22│$T22│$W22│$H22│$F22│$S22│$U22│\n\
├──────────┼&M22┼&T22┼&W22┼&H22┼&F22┼&S22┼&U22┤\n\
│  23:00   │$M23│$T23│$W23│$H23│$F23│$S23│$U23│\n\
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘"

TEXT_MENU = "\
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐\n\
│                                                                                                     │\n\
│                                         시간표 생성 프로그램                                        │\n\
│                                                                                                     │\n\
│                             - 건국대학교 전공기초프로젝트1 3239분반 4조 -                           │\n\
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤\n\
│                                                                                                     │\n\
│                                     ┌───────────────────────────┐                                   │\n\
│                                     │                           │                                   │\n\
│                                     │      1. 생 성 하 기       │                                   │\n\
│                                     │      2. 불 러 오 기       │                                   │\n\
│                                     │      3. 저 장 하 기       │                                   │\n\
│                                     │      4. 종 료 하 기       │                                   │\n\
│                                     │                           │                                   │\n\
│                                     └───────────────────────────┘                                   │\n\
│                                                                                                     │\n\
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘"


# ========== 시간 예측 모델 ===========
class Model_Time(object):

    # 딥러닝 네트워크 구축
    def __init__(self):
        self.X = tf.placeholder(tf.float32, shape=[None, 3]) # 입력 3 (0 ~ 2)
        self.Y = tf.placeholder(tf.float32, shape=[None, 15]) # 출력 15 (9 ~ 23)

        self.W1 = tf.Variable(tf.random_uniform([3, 15], -1., 1.))
        self.b1 = tf.Variable(tf.zeros([15]))
        self.L1 = tf.nn.relu(tf.add(tf.matmul(self.X, self.W1), self.b1))

        self.W2 = tf.Variable(tf.random_normal([15, 30]))
        self.b2 = tf.Variable(tf.zeros([30]))
        self.L2 = tf.nn.relu(tf.add(tf.matmul(self.L1, self.W2), self.b2))

        self.W3 = tf.Variable(tf.random_normal([30, 60]))
        self.b3 = tf.Variable(tf.zeros([60]))
        self.L3 = tf.nn.relu(tf.add(tf.matmul(self.L2, self.W3), self.b3))

        self.W4 = tf.Variable(tf.random_normal([60, 40]))
        self.b4 = tf.Variable(tf.zeros([40]))
        self.L4 = tf.nn.relu(tf.add(tf.matmul(self.L3, self.W4), self.b4))

        self.W5 = tf.Variable(tf.random_normal([40, 30]))
        self.b5 = tf.Variable(tf.zeros([30]))
        self.L5 = tf.nn.relu(tf.add(tf.matmul(self.L4, self.W5), self.b5))

        self.W6 = tf.Variable(tf.random_normal([30, 15]))
        self.b6 = tf.Variable(tf.zeros([15]))
        self.model = tf.add(tf.matmul(self.L5, self.W6), self.b6)

        # cost 계산
        self.cost = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits_v2(labels=self.Y, logits=self.model))
        
        # optimizer
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        self.train_op = self.optimizer.minimize(self.cost)


    # 학습 함수
    def TRAIN(self, x_data, y_data, iter):
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)
        # iter 번 학습 시행
        for step in range(iter):
            self.sess.run(self.train_op, feed_dict={self.X: x_data, self.Y: y_data})   
    

    # 예측 함수
    def PREDICT(self, x_data, y_data, p_data):
        self.TRAIN(x_data, y_data, 100) # 경험 집합 데이터 100번 학습
        self.prediction = tf.argmax(self.model, 1) 
        # 예측 시행
        return self.sess.run(self.prediction, feed_dict={self.X: p_data})
        self.sess.close()


# ========== 요일 예측 모델 ===========
class Model_Week(object):

    def __init__(self):
        self.X = tf.placeholder(tf.float32, shape=[None, 3])
        self.Y = tf.placeholder(tf.float32, shape=[None, 7])

        self.W1 = tf.Variable(tf.random_uniform([3, 15], -1., 1.))
        self.b1 = tf.Variable(tf.zeros([15]))
        self.L1 = tf.nn.relu(tf.add(tf.matmul(self.X, self.W1), self.b1))

        self.W2 = tf.Variable(tf.random_normal([15, 30]))
        self.b2 = tf.Variable(tf.zeros([30]))
        self.L2 = tf.nn.relu(tf.add(tf.matmul(self.L1, self.W2), self.b2))

        self.W3 = tf.Variable(tf.random_normal([30, 60]))
        self.b3 = tf.Variable(tf.zeros([60]))
        self.L3 = tf.nn.relu(tf.add(tf.matmul(self.L2, self.W3), self.b3))

        self.W4 = tf.Variable(tf.random_normal([60, 40]))
        self.b4 = tf.Variable(tf.zeros([40]))
        self.L4 = tf.nn.relu(tf.add(tf.matmul(self.L3, self.W4), self.b4))

        self.W5 = tf.Variable(tf.random_normal([40, 15]))
        self.b5 = tf.Variable(tf.zeros([15]))
        self.L5 = tf.nn.relu(tf.add(tf.matmul(self.L4, self.W5), self.b5))

        self.W6 = tf.Variable(tf.random_normal([15, 7]))
        self.b6 = tf.Variable(tf.zeros([7]))
        self.model = tf.add(tf.matmul(self.L5, self.W6), self.b6)

        self.cost = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits_v2(labels=self.Y, logits=self.model))
        
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        self.train_op = self.optimizer.minimize(self.cost)


    def TRAIN(self, x_data, y_data, iter):
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)
    
        for step in range(iter):
            self.sess.run(self.train_op, feed_dict={self.X: x_data, self.Y: y_data})   
    

    def PREDICT(self, x_data, y_data, p_data):
        self.TRAIN(x_data, y_data, 100)
        self.prediction = tf.argmax(self.model, 1)
        return self.sess.run(self.prediction, feed_dict={self.X: p_data})
        self.sess.close()


PAGE = 1 # 현재 페이지 (1 : 메인메뉴  / 2: 생성 페이지)

NOW_TODO = str(TEXT_TODO_HEADER) # 현재 할 일 테이블 텍스트
NOW_TABLE = str(TEXT_TABLE) # 현재 시간표 테이블 텍스트

# 할 일 리스트
todoList = list()
# 학습용 경험 집합
EXP_SET = list()

# 명령어 history
op_history = list()
op_history_idx = -1
op_temp_idx = 1

# 유저가 마지막으로 수정 후 저장 여부
user_save_check = None

# 학습용 모델
model_time = Model_Time() # 시간
model_week = Model_Week() # 요일

# epsilon
epsilon = 0.8


# todo 테이블에 할 일을 작성하는 함수
def WriteOnTodoTable(tasks):
    global NOW_TODO
    global TEXT_TODO_CENTER, TEXT_TODO_BOTTOM

    # 텍스트 초기화
    NOW_TODO = str(TEXT_TODO_HEADER)
    tempTODO = str(TEXT_TODO_CENTER)

    # 리스트 내 반복
    for task in tasks:
        tempTODO = str(TEXT_TODO_CENTER)

        # 내용
        text = task[0] + ' '*(10 - GetFixedLen(task[0]))
        tempTODO = tempTODO.replace("$T", text, 1)

        # 시작시각
        if task[2] is None:
            text = "          "
        else:
            h, m = str(task[2]), str(task[3])
            if len(h) == 1:
                h = '0' + h
            if len(m) == 1:
                m = '0' + m
            text = h + ':' + m + "     "
        tempTODO = tempTODO.replace("$S", text)

        # 지속시간
        if task[4] is None:
            text = "          "
        else:
            h, m = str(task[4]), str(task[5])
            if len(h) == 1:
                h = '0' + h
            if len(m) == 1:
                m = '0' + m
            text = h + ':' + m + "     "
        tempTODO = tempTODO.replace("$R", text)

        # 종료시각
        if (task[2] is None) or (task[4] is None):
            text = "          "
        else:
            sH, sM, rH, rM = task[2], task[3], task[4], task[5]
            m, h = sM + rM, sH + rH
            if m >= 60:
                h = h + (m // 60)
                m = m % 60
            h, m = str(h), str(m)
            if len(h) == 1:
                h = '0' + h
            if len(m) == 1:
                m = '0' + m
            text = h + ':' + m + "     "
        tempTODO = tempTODO.replace("$E", text)

        # 요일
        if task[6] is None:
            text = "                     "
        else:
            text = ', '.join(task[6])
            text = text + ' '*(21 - GetFixedLen(text))
        tempTODO = tempTODO.replace("$W", text)

        # 태그
        tags = ['#강의     ', '#과제     ', '#일과     ']
        tempTODO = tempTODO.replace("$G", tags[task[1]])

        # 서브태그
        if task[7] is None:
            text = "                        "
        else:
            text = task[7] + ' '*(24 - GetFixedLen(task[7]))
        tempTODO = tempTODO.replace("$D", text)

        NOW_TODO = NOW_TODO + '\n' + tempTODO

    # 텍스트 닫기
    completeTodo()
# End


# 시간표 테이블에 할 일을 추가하는 함수
def WriteOnTable(task):
    global NOW_TABLE

    sH, sM, rH, rM = task[2], task[3], task[4], task[5]
    eM, eH = sM + rM, sH + rH
    if eM >= 60:
        eH = eH + (eM // 60)
        eM = eM % 60

    # 30분만 지속하는 경우
    if rH == 0 and rM == 30:
        text = task[0] + '─'*(10 - GetFixedLen(task[0]))
    else:
        text = task[0] + ' '*(10 - GetFixedLen(task[0]))

    # 요일 별로 추가해주기
    for w in task[6]:
        ew = ['M', 'T', 'W', 'H', 'F', 'S', 'U']
        hw = ['월', '화', '수', '목', '금', '토', '일']
        w = ew[hw.index(w)]
        stime = str(sH)
        if len(stime) == 1:
            stime = '0' + stime

        tBox = '$' + w + stime
        tLine = '&' + w + stime

        if sM == 30:
            NOW_TABLE = NOW_TABLE.replace(tBox, BAR).replace(tLine, text)
        else:
            if (rH == 1 and rM == 0):
                NOW_TABLE = NOW_TABLE.replace(tBox, text).replace(tLine, BAR)
            else:
                NOW_TABLE = NOW_TABLE.replace(tBox, text).replace(tLine, SPC)

        for idx in range(sH + 1, eH - 1):
            stime = str(idx)
            if len(stime) == 1:
                stime = '0' + stime

            tBox = '$' + w + stime
            tLine = '&' + w + stime
            NOW_TABLE = NOW_TABLE.replace(tBox, SPC).replace(tLine, SPC)

        if eM == 30:
            stime = str(eH)
            if len(stime) == 1:
                stime = '0' + stime

            tBox = '$' + w + stime
            tLine = '&' + w + stime
            NOW_TABLE = NOW_TABLE.replace(tBox, BAR).replace(tLine, BAR)

            stime = str(eH - 1)
            if len(stime) == 1:
                stime = '0' + stime

            tLine = '&' + w + stime
            NOW_TABLE = NOW_TABLE.replace(tLine, SPC)
# End of DEF WriteOnTable


# ========== 시간표 생성 마무리 ===========
def completeTable():
    global NOW_TABLE
    week = ['M', 'T', 'W', 'H', 'F', 'S', 'U']

    for w in week:
        for i in range(9, 24):
            j = str(i)
            if len(j) == 1:
                j = '0' + j
            tBox = '$' + w + j
            tLine = '&' + w + j
            NOW_TABLE = NOW_TABLE.replace(tBox, SPC).replace(tLine, BAR)

    NOW_TABLE = NOW_TABLE.replace(' ┼', ' ├').replace(
        '┼ ', '┤ ').replace(' ├ ', ' │ ')
    NOW_TABLE = NOW_TABLE.replace('│─', '├─').replace('─│', '─┤')
# End of DEF CompleteTable


# ========== 할 일 테이블 생성 마무리 ===========
def completeTodo():
    global NOW_TODO
    global TEXT_TODO_BOTTOM
    NOW_TODO = NOW_TODO + '\n' + TEXT_TODO_BOTTOM
# End of DEF CompleteTodo


# ========== 시간표에 대상 추가 ===========
def AddTable(tasks):

    global model_time, model_week, epsilon, NOW_TABLE, TEXT_TABLE

    NOW_TABLE = TEXT_TABLE

    # [0]  / [1]  / [2]    [3]    / [4]     [5]    / [6]   / [7]
    # 내용 / 태그  / 시작시 시작분  / 지속시  지속분  / 요일  / 서브태그    
    for task in tasks:
        
        # 지속 시각 예측이 필요한 경우
        if (task[4] is None):
            task[4] = randrange(1, 3)
            task[5] = choice([0, 30])

        # 지속 시간 이외 고정인 경우
        if (task[2] is None) or (task[6] is None):
            # 태그 -> One Hot Enc
            tempTag = [0, 0, 0]
            tempTag[task[1]] = 1
            p_data = np.array([tempTag])

            if len(EXP_SET) == 0:
                x_data = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
                y_time_data = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]])
                y_week_data = np.array([[0, 1, 0, 0, 0, 0, 0], 
                                        [0, 0, 0, 1, 0, 0, 0], 
                                        [0, 0, 0, 0, 0, 1, 0]])
            else:
                l_tag, l_time, l_week = [], [], []

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

            # 시작시각 예측이 필요한 경우
            if (task[2] is None):
                if random() < epsilon:
                    task[2] = int(model_time.PREDICT(x_data, y_time_data, p_data)) + 9
                    task[3] = choice([0, 30])
                else:
                    task[2] = randrange(9, 22)
                    task[3] = choice([0, 30])

            # 요일 예측이 필요한 경우
            if (task[6] is None):
                if random() < epsilon:
                    hw = ['월', '화', '수', '목', '금', '토', '일']
                    task[6] = list(hw[int(model_week.PREDICT(x_data, y_week_data, p_data))])
                else:
                    task[6] = list(choice(['월', '화', '수', '목', '금', '토', '일']))
                
        print(task)
        if (task[2] is not None) and (task[4] is not None) and (task[6] is not None):
            WriteOnTable(task)
            EXP_SET.append(task)
        else:
            print("알 수 없는 오류 발생") # 이 오류가 발생한다면 프로그램 자체에 중대한 오류가 있는 것.

        epsilon -= 0.0001 # 입실론 조정
# END of DEF AddTable


# ========== PyQt5 GUI 프로그램 클래스 ===========
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # Set Window
        self.setWindowTitle('시간표 생성 프로그램')
        self.resize(960, 720)

        # Set Layout
        grid = QGridLayout()
        self.setLayout(grid)

        # TextBrowser
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(False)

        # LineEdit
        self.opline = QLineEdit()
        self.opline.setPlaceholderText("선택 : ")
        self.opline.editingFinished.connect(self.opEntered)

        # Add Widget
        grid.addWidget(self.tb, 0, 0)
        grid.addWidget(self.opline, 1, 0)
        self.show()


    # ========== 닫는 이벤트 발생 시 호출 ===========
    def closeEvent(self, event):
        # TODO
        global user_save_check

        if user_save_check:
            reply = QMessageBox.question(self, '종료', '저장되지 않은 변경 사항은 삭제됩니다. 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()


    # ========== 텍스트 브라우저 초기화 ===========
    def clearScreen(self):
        self.tb.clear()


    # ========== 텍스트 브라우저에 텍스트 표시 (리셋) ===========
    def setText(self, text):
        self.tb.clear()
        self.tb.setText(text)


    # ========== 텍스트 브라우저에 텍스트 추가 (리셋 X) ===========
    def appendText(self, text):
        self.tb.append(text)


    # ========== 오류 메세지 출력 함수 ===========
    def addError(self, text):
        self.tb.append('\n\n')
        self.tb.append('<p style="color: red">' + text + '</p>')


    # ========== 명령어 히스토리 이동 (방향키) ===========
    def keyPressEvent(self, e):
        global op_temp_idx, op_history, op_history_idx

        if e.key() == Qt.Key_Up:
            if (op_temp_idx > 0):
                op_temp_idx -= 1
                self.opline.setText(op_history[op_temp_idx])

        elif e.key() == Qt.Key_Down:
            if (op_temp_idx < op_history_idx):
                op_temp_idx += 1
                self.opline.setText(op_history[op_temp_idx])
            elif (op_temp_idx == op_history_idx):
                self.opline.setText('')


    # ========== 엔터키 입력 시 호출 ===========
    def opEntered(self):

        global NOW_TODO, todoList, PAGE, user_save_check
        global op_history, op_history_idx, op_temp_idx

        opstr = self.opline.text()
        oplist = list(map(str, opstr.split()))

        # ========== 예외 ===========
        if opstr is None or opstr == '':
            return
        
        op_history.append(opstr)
        op_history_idx += 1
        op_temp_idx = op_history_idx + 1

        # # ========== 메뉴 페이지 ===========
        if PAGE == 1:
            # ========== 생성하기 ===========
            if oplist[0] == '1':
                self.resetLine()
                PAGE = 2
                self.opline.setPlaceholderText("명령어 : ")
                WriteOnTodoTable(todoList)
                self.setText(NOW_TODO)


            # ========== 불러오기 ===========
            elif oplist[0] == '2':
                self.resetLine()


            # ========== 저장하기 ===========
            elif oplist[0] == '3':
                self.resetLine()
                user_save_check = False


            # ========== 종료하기 ===========
            elif oplist[0] == '4':
                self.resetLine()
                

            else:
                self.resetLine()
                self.setText(TEXT_MENU)
                self.addError('오류: 올바른 메뉴를 선택하세요.')


        # ========== 생성 페이지 ===========
        elif PAGE == 2:
            # ========== 도움말 ===========
            if oplist[0] == '/도움말':
                self.resetLine()
                self.setText(TEXT_HELP)


            # ========== 추가 ===========
            elif oplist[0] == '/추가':
                self.resetLine()
                if len(oplist) == 9:
                    todoList.append([oplist[1], int(oplist[2]), int(oplist[3]), int(oplist[4]), int(oplist[5]), int(oplist[6]), [oplist[7]], oplist[8]])

                user_save_check = True
                WriteOnTodoTable(todoList)
                self.setText(NOW_TODO)


            # ========== 테스트 데이터 추가 ===========
            elif oplist[0] == '/테스트':
                self.resetLine()
                todoList.append(['할일1', 0, 9, 30, 0, 30, ['월'], '내용1'])
                todoList.append(['할일2', 0, 10, 0, 1, 0, ['화'], '내용2'])
                todoList.append(['할일3', 1, None, None, 1, 0, ['수', '금'], '내용3'])
                todoList.append(['할일4', 2, 9, 30, 0, 30, None, '내용4'])
                todoList.append(['할일5', 1, 16, 30, None, None, ['화', '토'], '내용5'])
                todoList.append(['할일6', 0, None, None, None, None, ['목', '일'], '내용6'])
                todoList.append(['할일7', 1, None, None, None, None, None, None])

                user_save_check = True
                WriteOnTodoTable(todoList)
                self.setText(NOW_TODO)


            # ========== 뒤로가기 ===========
            elif oplist[0] == '//':
                self.opline.setPlaceholderText("선택 : ")
                self.resetLine()
                self.setText(TEXT_MENU)
                PAGE = 1


            # ========== 입력완료 ===========
            elif oplist[0] == '/입력완료':
                self.resetLine()
                
                if len(todoList) == 0:
                    self.addError('오류: 추가된 할 일이 없어 시간표를 생성할 수 없습니다.')
                else:
                    AddTable(todoList)
                    completeTable()
                    self.setText(NOW_TABLE)


            # ========== 수정 ===========
            elif oplist[0] == '/수정':
                self.resetLine()

                pass


            # ========== 삭제 ===========
            elif oplist[0] == '/삭제':
                self.resetLine()
                    
                if len(todoList) == 0:
                    infoText = '\n\n오류: 추가한 할 일이 없습니다.'

                elif len(oplist) == 1:
                    reply = QMessageBox.question(self, '경고', '할 일을 전부 삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    deleteFlag = (reply == QMessageBox.Yes)
                    if deleteFlag:
                        todoList = list()
                        infoText = '\n\n할 일을 전부 삭제했습니다.'
                        user_save_check = True
                    else:
                        infoText = ''

                elif GetFixedLen(oplist[1]) > 10:
                    infoText = '\n\n오류: 검색어의 고정폭 길이는 10을 초과할 수 없습니다.'

                else:
                    todo = ''
                    for i in range(1, len(oplist), 1):
                        todo += oplist[i] + ' '
                    todo = todo.strip()

                    found = False
                    i = 0
                    while(i < len(todoList)):
                        if(todoList[i][0] == todo):
                            del todoList[i]
                            found = True
                        else:
                            i += 1

                    if(found == True):
                        infoText = '\n\n\'' + todo + '\'을(를) 모두 삭제하였습니다.'
                        user_save_check = True
                    elif(found == False):
                        infoText = '\n\n경고: 일치하는 할 일이 없습니다. 데이터를 삭제하지 않았습니다.'

                WriteOnTodoTable(todoList)
                self.setText(NOW_TODO)
                self.addError(infoText)


            # ========== 검색 ===========
            elif oplist[0] == '/검색':
                self.resetLine()
                searchedList = list()

                tmpStr = ''.join(oplist)[3:] # '/검색'을 제외하고 공백을 없앤 후 합친 문자열
                if tmpStr == '': # /검색만 치고 내용을 입력 안 한 케이스
                    self.setText(NOW_TODO)
                    self.addError('오류: 검색할 내용을 1자 이상 입력하세요.')
                    return
                else:
                    tmpList = tmpStr.split('-') # 리스트에 원소가 2개인지 체크해서 2개가 아니면 에러(하이픈이 2개 이상 들어온거)
                    if len(tmpList) > 1:               # '-'뒤에 정수를 입력한 경우
                        searchNum = int(tmpList[1])
                    else:                              # '-' + 정수를 입력하지 않은 경우
                        searchNum = 1
                    
                    searchString = compressWord(tmpList[0])

                    for todo in todoList:
                        count = 0
                        cmpString = compressWord(todo[0]) # 공백과 겹치는 문자를 제거한 '할 일' 문자열

                        for cs in cmpString:
                            for ss in searchString:  # 한 글자씩 비교해서 searchNum까지 count 증가시키기
                                if ss==cs:
                                    count += 1
                        
                        if count >= searchNum:       # 겹치는 글자가 기준을 충족한 경우
                            searchedList.append(todo)

                    if (len(searchedList) == 0):
                        WriteOnTodoTable(todoList)
                        self.setText(NOW_TODO)
                        self.addError('검색 결과가 없습니다.')
                    else:
                        WriteOnTodoTable(searchedList)
                        self.setText('검색 결과 : \n\n' + NOW_TODO)


            # ========== 예외 ===========
            else:
                completeTable()
                self.setText(NOW_TODO)
                self.addError('오류: 인식할 수 없는 명령어입니다.')

        self.resetLine()
        oplist = None


    # ========== 명령문 입력줄 초기화 ===========
    def resetLine(self):
        self.opline.clear()


    # ========== 메뉴 출력 함수 ===========
    def printMenu():
        self.setText(TEXT_MENU)


# 고정폯 글꼴 길이 반환 (한글은 2 나머지 1) 함수
def GetFixedLen(s):
    l = 0
    for _ in s:
        if (_ == ' ' or _ == ','):
            l += 1
        elif (_.encode().isalnum()):
            l += 1
        else:
            l += 2
    return l


# ========== 문자열 압축 함수 ===========
def compressWord(i):
    s = ''.join(set(i))
    return s


# ========== 패키지 설치 점검 및 설치 (미사용) ===========
"""def pip_install(package):
    installed = False
    try:
        subprocess.check_call(["pip", "install", package])
        installed = True
    except Exception as e:
        print(e)
        installed = False

    if not installed:
        try:
            subprocess.check_call(["pip3", "install", package])
        except Exception as e:
            installed = False
            print(e)
"""

# ========== 메인 ===========
def main():
# package check - tensorflow
    """try:
        import tensorflow as tf
        print('tensorflow installed')
    except Exception as e:
        print(e)
        pip_install('tensorflow==1.15.*')

    # package check - PyQt5
    try:
        import PyQt5
        print('PyQt5 installed')
    except Exception as e:
        print(e)
        pip_install('PyQt5')"""

    # App Instance
    _ = QApplication(sys.argv)
    app = App()

    global user_save_check
    user_save_check = False

    app.setText(TEXT_MENU)

    # Font
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./D2Coding.ttf')
    _.setFont(QFont('D2Coding'))

    # exit
    sys.exit(_.exec_())


if __name__ == '__main__':
    main()
    
# EOF
