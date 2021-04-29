#-*-coding:utf-8-*-

import PyQt5
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser, QMessageBox, QFileDialog)
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
/입력완료 : 할 일을 모두 입력한 후 시간표를 생성하기 위해 사용한다. 인자는 없다.\n\
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
1. // : 뒤로가기 명령어. 이전 페이지로 이동한다.\n"

BAR = "──────────"
SPC = "          "

TEXT_TODO_HEADER = "\
┌──────────┬──────────┬──────────┬──────────┬─────────────────────┬──────────┬────────────────────────┐\n\
│  할 일   │ 시작시각 │ 지속시간 │ 종료시각 │       요  일        │   태그   │        서브태그        │"

TEXT_TODO_CENTER = "\
├──────────┼──────────┼──────────┼──────────┼─────────────────────┼──────────┼────────────────────────┤\n\
│$T│$S│$R│$E│$W│$G│$D│"

TEXT_TODO_BOTTOM = "\
└──────────┴──────────┴──────────┴──────────┴─────────────────────┴──────────┴────────────────────────┘\n\
\n\
* 빈 칸은 고정하지 않은 정보를 나타냅니다. \n\
* 할 일을 모두 입력한 후 /생성 명령으로 시간표를 생성하세요."

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
│                            * 도움말을 읽으려면 /도움말 명령어를 입력하세요.                         │\n\
│                                                                                                     │\n\
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘"


# ========== 시간 예측 모델 ===========
class Model_Time(object):

    # 딥러닝 네트워크 구축
    def __init__(self):
        self.X = tf.placeholder(tf.float32, shape=[None, 3])  # 입력 3 (0 ~ 2)
        self.Y = tf.placeholder(tf.float32, shape=[None, 15])  # 출력 15 (9 ~ 23)

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
            self.sess.run(self.train_op, feed_dict={
                          self.X: x_data, self.Y: y_data})

    # 예측 함수

    def PREDICT(self, x_data, y_data, p_data):
        self.TRAIN(x_data, y_data, 100)  # 경험 집합 데이터 100번 학습
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
            self.sess.run(self.train_op, feed_dict={
                          self.X: x_data, self.Y: y_data})

    def PREDICT(self, x_data, y_data, p_data):
        self.TRAIN(x_data, y_data, 100)
        self.prediction = tf.argmax(self.model, 1)
        return self.sess.run(self.prediction, feed_dict={self.X: p_data})
        self.sess.close()


PAGE = 1  # 현재 페이지 (1 : 메인메뉴  / 2: 생성 페이지)

NOW_TODO = str(TEXT_TODO_HEADER)  # 현재 할 일 테이블 텍스트
NOW_TABLE = str(TEXT_TABLE)  # 현재 시간표 테이블 텍스트

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
user_table_make = False

# 학습용 모델
model_time = Model_Time()  # 시간
model_week = Model_Week()  # 요일

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

        if (task[5] is None):
            task[5] = 0

        # 지속 시간 이외 고정인 경우
        if (task[2] is None) or (task[6] is None):
            # 태그 -> One Hot Enc
            tempTag = [0, 0, 0]
            tempTag[task[1]] = 1
            p_data = np.array([tempTag])

            if len(EXP_SET) == 0:
                x_data = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
                y_time_data = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 1,
                                            0, 0, 0, 0, 0, 0, 0],
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
                    task[2] = int(model_time.PREDICT(
                        x_data, y_time_data, p_data)) + 9
                    task[3] = choice([0, 30])
                else:
                    task[2] = randrange(9, 22)
                    task[3] = choice([0, 30])

            # 요일 예측이 필요한 경우
            if (task[6] is None):
                if random() < epsilon:
                    hw = ['월', '화', '수', '목', '금', '토', '일']
                    task[6] = list(
                        hw[int(model_week.PREDICT(x_data, y_week_data, p_data))])
                else:
                    task[6] = list(choice(['월', '화', '수', '목', '금', '토', '일']))

        print(task)
        if (task[2] is not None) and (task[4] is not None) and (task[6] is not None):
            WriteOnTable(task)
            EXP_SET.append(task)
        else:
            print("알 수 없는 오류 발생")  # 이 오류가 발생한다면 프로그램 자체에 중대한 오류가 있는 것.

        epsilon -= 0.0001  # 입실론 조정
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
            reply = QMessageBox.question(
                self, '종료', '저장되지 않은 변경 사항은 삭제됩니다. 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
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

        global NOW_TODO, todoList, PAGE, user_save_check, NOW_TABLE, TEXT_TABLE
        global op_history, op_history_idx, op_temp_idx, user_table_make

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
            # ========== 도움말 ===========
            if oplist[0] == '/도움말':
                self.resetLine()
                self.setText(TEXT_HELP)
            # ========== 생성하기 ===========
            elif oplist[0] == '1':
                self.resetLine()
                PAGE = 2
                self.opline.setPlaceholderText("명령어 : ")
                WriteOnTodoTable(todoList)
                self.setText(NOW_TODO)

            # ========== 불러오기 ===========
            elif oplist[0] == '2':
                self.resetLine()
                # .tbl .tds
                fname = QFileDialog.getOpenFileName(self, '불러오기', './', '*.tbl *.tds')
                
                if fname[0]:
                    if fname[0].split('.')[-1] == 'tbl':
                        f = open(fname[0], 'r', encoding='utf-8')
                        data = f.read()
                        if data == '' or data == None:
                            self.addError("오류: 빈 파일이거나 손상된 파일이므로 불러올 수 없습니다.")
                        else:
                            NOW_TABLE = data
                            PAGE = 2
                            f.close()
                            self.setText(NOW_TABLE)
                    else:
                        f = open(fname[0], 'r', encoding='utf-8')
                        datas = f.readlines()
                        if len(datas) == 0 or datas == None:
                            self.addError("오류: 빈 파일이거나 손상된 파일이므로 불러올 수 없습니다.")
                        else:
                            PAGE = 2
                            newDatas = []
                            for todo in datas:
                                tlist = todo.split(',')

                                for i in range(8):
                                    if tlist[i] == 'None':
                                        tlist[i] = None

                                if tlist[1] != None:
                                    tlist[1] = int(tlist[1])

                                if tlist[2] != None:
                                    tlist[2] = int(tlist[2])

                                if tlist[3] != None:
                                    tlist[3] = int(tlist[3])

                                if tlist[4] != None:
                                    tlist[4] = int(tlist[4])

                                if tlist[5] != None:
                                    tlist[5] = int(tlist[5])

                                if tlist[6] != None:
                                    tlist[6] = tlist[6].split('&')

                                if tlist[7] != None:
                                    tlist[7] = tlist[7].replace('\n', '')

                                newDatas.append(tlist)

                            print(newDatas)
                            todoList = newDatas
                            user_save_check = True
                            WriteOnTodoTable(todoList)
                            self.setText(NOW_TODO)


            # ========== 저장하기 ===========
            elif oplist[0] == '3':
                self.resetLine()
                fname = QFileDialog.getSaveFileName(self, '저장하기', './')
                print(fname)
                user_save_check = False

                infoText = ''
                if todoList == None or len(todoList) == 0:
                    infoText = '경고: 추가된 할 일이 없어 할 일 파일을 저장하지 않았습니다.'
                else:
                    t = ''

                    for todo in todoList:
                        t += todo[0] + ','
                        t += str(todo[1]) + ','
                        if todo[2] != None:
                            t += str(todo[2]) + ','
                        else:
                            t += 'None,'
                        
                        if todo[3] != None:
                            t += str(todo[3]) + ','
                        else:
                            t += 'None,'
                            
                        if todo[4] != None:
                            t += str(todo[4]) + ','
                        else:
                            t += 'None,'

                        if todo[5] != None:
                            t += str(todo[5]) + ','
                        else:
                            t += 'None,'

                        if todo[6] != None:
                            t += str('&'.join(todo[6])) + ','
                        else:
                            t += 'None,'

                        if todo[7] != None:
                            t += todo[7] + '\n'
                        else:
                            t += 'None\n'
                    
                    f = open(fname[0] + '.tds', mode='wt', encoding='utf-8')
                    f.write(t)
                    f.close()

                    self.appendText('\n할 일 파일 : ' + fname[0] + '.tds 파일을 저장하였습니다.')

                if user_table_make == False:
                    if infoText != '':
                        infoText += '\n\n'
                    infoText += '경고: 생성된 테이블이 없어 파일을 저장하지 않았습니다.'
                else:
                    f = open(fname[0] + '.tbl', mode='wt', encoding='utf-8')
                    f.write(NOW_TABLE)
                    f.close()

                    self.appendText('\n시간표 파일 : ' + fname[0] + '.tbl 파일을 저장하였습니다.')
                
                if infoText != '':
                    self.addError(infoText)

            # ========== 종료하기 ===========
            elif oplist[0] == '4':
                self.resetLine()

                if user_save_check:
                    reply = QMessageBox.question(self, '종료', '저장되지 않은 변경 사항은 삭제됩니다. 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        exit(0)
                else:
                    exit(0)

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
                index = 0
                inputList = []
                timeList = []
                checker = True  # 오류 존재여부 확인

                index = 0
                for i in oplist:  # 할 일 내용 하나로 묶어주기
                    todo = ""  # 할 일
                    if ('#' in i) or ('{' in i):
                        for k in range(1, index):
                            todo += oplist[k] + " "

                        for k in range(1, index):  # oplist에서 할 일 data 삭제
                            del oplist[1]
                        break

                    index += 1
                inputList.append(todo.strip())

                index = 0
                for i in oplist:  # 필수 태그 추출
                    if '#' in i:
                        tagList = ['#강의', '#과제', '#일과']
                        if i not in tagList:
                            infoText = "오류: 필수태그가 #강의, #과제, #일과 중 하나가 아닙니다."
                            self.addError(infoText)
                            checker = False
                            return
                        else:
                            inputList.append(tagList.index(i))
                        del oplist[index]  # oplist에서 필수 태그 data 삭제
                        break
                    elif (not('#' in ' '.join(oplist))):
                        inputList.append(None)
                        break
                    index += 1

                index = 0
                openIndex = 0
                closeIndex = 0
                for i in oplist:  # {시간 데이터}를 timeList에 따로 분리
                    if ('{' in i):
                        openIndex = index
                    if ('}' in i):
                        closeIndex = index
                    index += 1

                if (openIndex != closeIndex or (openIndex != 0 and closeIndex != 0 and len(oplist[openIndex]) > 2)) and (openIndex != 0 and closeIndex != 0):
                    for k in range(openIndex, closeIndex + 1):
                        if oplist[k].replace("{", "").replace("}", "") != '':
                            timeList.append(oplist[k].replace("{", "").replace("}", ""))

                    # oplist에서 {시간 데이터} data 삭제
                    for k in range(openIndex, closeIndex + 1):
                        del oplist[openIndex]

                    if timeList:
                        index = 0
                        if not timeList:
                            inputList.append(None)
                        else:
                            for i in timeList:  # 시간 데이터 분류 '시'
                                if '분' in i or '반' in i:
                                    self.addError(
                                        "오류: '시작시간(분)' 정보가 '시작시간(시)' 정보보다 앞에 있거나 띄어쓰기 없이 붙어 있습니다.")
                                    checker = False
                                    del timeList[index]
                                    inputList.append(None)
                                    break
                                if i.replace('시', '').replace("시간", "") == "":
                                    inputList.append(None)
                                    break
                                if ('시' in i) and i.replace('시', '').replace("시간", "") != "":
                                    inputList.append(
                                        int(i.replace('시', '').replace("시간", "")))
                                    del timeList[index]
                                    break
                                elif (not('시' in ' '.join(timeList))):
                                    inputList.append(None)
                                    break

                                index += 1

                        index = 0
                        if not timeList:
                            inputList.append(None)
                        else:
                            for i in timeList:  # 시간 데이터 분류 '분'
                                if i.replace("분", "") == "":
                                    inputList.append(None)
                                    break
                                if ('분' in i) and i.replace("분", "") != "":
                                    inputList.append(int(i.replace("분", "")))
                                    del timeList[index]
                                    break
                                if ('반' in i):
                                    inputList.append(30)
                                    del timeList[index]
                                    break
                                elif (not('분' in ' '.join(timeList)) and not('반' in ' '.join(timeList))):
                                    inputList.append(None)
                                    break

                                index += 1

                        index = 0
                        if not timeList:
                            inputList.append(None)
                        else:
                            for i in timeList:  # 시간 데이터 분류 'h'
                                if 'm' in i:
                                    self.addError(
                                        "오류: '지속시간(m)' 정보가 '지속시간(h)' 정보보다 앞에 있거나 띄어쓰기 없이 붙어 있습니다.")
                                    checker = False
                                    del timeList[index]
                                    inputList.append(None)
                                    break
                                if i.replace("h", "") == "":
                                    inputList.append(None)
                                    break
                                if ('h' in i) and i.replace("h", "") != "":
                                    inputList.append(int(i.replace("h", "")))
                                    del timeList[index]
                                    break
                                elif (not('h' in ' '.join(timeList))):
                                    inputList.append(None)
                                    break

                                index += 1

                        index = 0
                        if not timeList:
                            inputList.append(None)
                        else:
                            for i in timeList:  # 시간 데이터 분류 'm'
                                if i.replace("m", "") == "":
                                    inputList.append(None)
                                    break
                                if ('m' in i) and i.replace("m", "") != "":
                                    inputList.append(int(i.replace("m", "")))
                                    del timeList[index]
                                    break
                                elif (not('m' in ' '.join(timeList))):
                                    inputList.append(None)
                                    break

                                index += 1

                        index = 0
                        if not timeList:
                            inputList.append(None)
                        else:
                            weekList = []
                            for i in timeList:  # 시간 데이터 분류 '요일'
                                if ("월요일" == i or "월" == i):
                                    weekList.append("월")
                                elif ("화요일" == i or "화" == i):
                                    weekList.append("화")
                                elif ("수요일" == i or "수" == i):
                                    weekList.append("수")
                                elif ("목요일" == i or "목" == i):
                                    weekList.append("목")
                                elif ("금요일" == i or "금" == i):
                                    weekList.append("금")
                                elif ("토요일" == i or "토" == i):
                                    weekList.append("토")
                                elif ("일요일" == i or "일" == i):
                                    weekList.append("일")

                                index += 1

                            if weekList:
                                inputList.append(weekList)
                            else:
                                inputList.append(None)
                else:
                    inputList.append(None)
                    inputList.append(None)
                    inputList.append(None)
                    inputList.append(None)
                    inputList.append(None)
                    if openIndex != 0:
                        del oplist[openIndex]

                index = 0
                start_index = 0
                for i in oplist:  # 서브 태그 추출
                    if '-' in i:
                        start_index = index
                        sstr = ""  # 서브 태그 합쳐서 저장
                        for k in range(start_index, len(oplist)):
                            sub_str = oplist[k].replace("-", "")
                            sstr += sub_str
                            if k != len(oplist) - 1:
                                sstr += " "
                        inputList.append(sstr)
                        for k in range(start_index, len(oplist)):
                            del oplist[index]
                        break
                    elif (not('-' in ' '.join(oplist))):
                        inputList.append(None)
                        break
                    index += 1

                print(inputList)
                #문법 규칙 확인
                infoText = ""

                if inputList[0] != None and GetFixedLen(inputList[0]) > 10:
                    infoText = "오류: 할일의 고정폭 길이가 10 초과!!! 현재 길이: " + \
                        str(GetFixedLen(inputList[0]))
                    self.addError(infoText)
                    checker = False
                if inputList[7] != None and GetFixedLen(inputList[7]) > 24:
                    infoText = "오류: 서브태그의 고정폭 길이가 24 초과!!! 현재 길이: " + \
                        str(GetFixedLen(inputList[7]))
                    self.addError(infoText)
                    checker = False
                if inputList[1] == None:
                    infoText = "오류: 필수태그 누락"
                    self.addError(infoText)
                    checker = False
                if inputList[2] != None and (inputList[2] > 24 or inputList[2] < 1):
                    infoText = "오류: 시작시간(시) 범위 초과!!! 1 이상 24 이하의 값을 입력해 주세요."
                    self.addError(infoText)
                    checker = False
                if inputList[3] != None and (inputList[3] != 0 and inputList[3] != 30):
                    infoText = "오류: 시작시간(분) 오류!!! 0 또는 30을 입력해 주세요."
                    self.addError(infoText)
                    checker = False

                if checker:
                    todoList.append(inputList)
                    user_save_check = True
                    WriteOnTodoTable(todoList)
                    print(todoList)
                    self.setText(NOW_TODO)

            # ========== 테스트 데이터 추가 ===========
            elif oplist[0] == '/테스트':
                self.resetLine()
                todoList.append(['할일1', 0, 9, 30, 0, 30, ['월'], '내용1'])
                todoList.append(['할일2', 0, 10, 0, 1, 0, ['화'], '내용2'])
                todoList.append(
                    ['할일3', 1, None, None, 1, 0, ['수', '금'], '내용3'])
                todoList.append(['할일4', 2, 9, 30, 0, 30, None, '내용4'])
                todoList.append(
                    ['할일5', 1, 16, 30, None, None, ['화', '토'], '내용5'])
                todoList.append(
                    ['할일6', 0, None, None, None, None, ['목', '일'], '내용6'])
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
                    user_table_make = True

            # ========== 수정 ===========
            # 일치하는 할일ㅇ, 할일 입력여부ㅇ, 해당하는 구성요소 지칭어ㅇ, 구성요소 지칭어 입력여부ㅇ, 수정할 내용 입력여부, 지칭어에 알맞은접접확인ㅇ
            elif oplist[0] == '/수정':
                self.resetLine()
                transIndex = 0  # 수정하고자 하는 할일의 todoList[] 인덱스 값
                infoText = ''

                if len(todoList) == 0:
                    infoText = '오류: 할 일이 없습니다.'

                elif len(oplist) == 1:
                    infoText = '오류: 수정할 할 일의 내용을 입력해주세요.'

                elif GetFixedLen(oplist[1]) > 10:
                    infoText = '오류: 검색어의 고정폭 길이는 10을 초과할 수 없습니다.'

                else:
                    toModify = ''
                    for i in range(1, len(oplist), 1):
                        toModify += oplist[i] + ' '
                    toModify = toModify.strip()
                    foundTodo = False  # 첫번째 인덱스의 내용(할일) 일치여부 확인
                    i = 0
                    while(i < len(todoList)):
                        if(todoList[i][0] == toModify.split(' ')[0]):
                            transIndex = i
                            foundTodo = True
                            break
                        else:
                            i += 1

                    cIndex = 0  # 구성요소 지칭어에따른 todoList[transIndex][cIndex] 위치
                    # 0할일 1필수태그 2시작시각(시) 3시작시작(분) 4지속시간(h) 5지속시간(m) 6요일집합{} 7서브태그
                    minIndex = 0  # 시작시각과 지속시간을 수정하고자 할 때 '분'에 해당하는 인덱스

                    rToMod = False  # 모든구문을 통과하여 수정 직전에 True

                    if foundTodo == True:  # 일치하는 할일 발견
                        c1 = ""  # 할 일
                        c2 = ""  # 구성요소 지칭어 (ex 요일, 태그, 시작시각..)
                        c3 = ""  # 수정할 내용
                        c1 = toModify[toModify.find(" "):toModify.find("-")-1]
                        c1 = c1.strip()

                        c2 = toModify[toModify.find(
                            "-"):toModify.find(" ", toModify.find("-"))]
                        c2 = c2.strip()

                        c3 = toModify[toModify.find(" ", toModify.find("-")):]
                        c3 = c3.strip()

                        if c2 == "-요일":
                            cIndex = 6
                            if todoList[transIndex][cIndex] == None:  # 수정대상이 None값인 경우
                                infoText = '오류: 해당하는 구성요소 지칭어가 없습니다.'

                            elif c3[0] == "{" and c3[len(c3)-1] == "}":

                                afterModList = []  # 리스트의 경우에는 afterModList 나머지는 afterMod /최종변경될 값을 여기에 저장
                                index = 0
                                for i in c3.split(" "):  # 시간 데이터 분류 '요일'
                                    i = i.replace("}", "").replace(
                                        "{", "").replace("-", "")
                                    if ("월요일" == i or "월" == i):
                                        afterModList.append(i)
                                    elif ("화요일" == i or "화" == i):
                                        afterModList.append(i)
                                    elif ("수요일" == i or "수" == i):
                                        afterModList.append(i)
                                    elif ("목요일" == i or "목" == i):
                                        afterModList.append(i)
                                    elif ("금요일" == i or "금" == i):
                                        afterModList.append(i)
                                    elif ("토요일" == i or "토" == i):
                                        afterModList.append(i)
                                    elif ("일요일" == i or "일" == i):
                                        afterModList.append(i)

                                    index += 1

                            #temptList = todoList[transIndex]
                            else:
                                infoText = '오류: 구성요소 지칭어에 알맞은 접두, 접미어가 아닙니다.'

                            if rToMod == True:
                                # 본 시간표에 수정
                                todoList[transIndex][cIndex] = afterModList

                        elif c2 == "-시작시각":
                            cIndex = 2
                            minIndex = 3
                            if todoList[transIndex][cIndex] == None:  # 수정대상이 None값인 경우
                                infoText = '오류: 해당하는 구성요소 지칭어가 없습니다.'

                            if c3[0] == "{" and c3[len(c3)-1] == "}":
                                if c3.find("분") > 0:
                                    minIndex = 5

                                afterModList = []
                                c3 = c3.replace("}", "")
                                c3 = c3.replace("{", "")
                                c3 = c3.replace(" ", "")
                                c3 = c3.replace("시", " ")
                                c3 = c3.replace("분", "")
                                afterModList = c3.split(" ")

                            else:
                                infoText = '오류: 구성요소 지칭어에 알맞은 접두, 접미어가 아닙니다.'

                            if rToMod == True:
                                # 본 시간표에 수정
                                todoList[transIndex][cIndex] = afterModList[0]
                                todoList[transIndex][minIndex] = afterModList[1]

                        elif c2 == "-지속시간":
                            cIndex = 4
                            if todoList[transIndex][cIndex] == None:  # 수정대상이 None값인 경우
                                infoText = '오류: 해당하는 구성요소 지칭어가 없습니다.'

                            if c3[0] == "{" and c3[len(c3)-1] == "}":
                                if c3.find("m") > 0:
                                    minIndex = 5

                                afterModList = []
                                c3 = c3.replace("}", "")
                                c3 = c3.replace("{", "")
                                c3 = c3.replace(" ", "")
                                c3 = c3.replace("h", " ")
                                c3 = c3.replace("m", "")
                                afterModList = c3.split(" ")

                            else:
                                infoText = '오류: 구성요소 지칭어에 알맞은 접두, 접미어가 아닙니다.'

                            if rToMod == True:
                                # 본 시간표에 수정
                                todoList[transIndex][cIndex] = afterModList[0]
                                todoList[transIndex][minIndex] = afterModList[1]

                        elif c2 == "-필수태그":
                            cIndex = 1
                            if todoList[transIndex][cIndex] == None:  # 수정대상이 None값인 경우
                                infoText = '오류: 해당하는 구성요소 지칭어가 없습니다.'
                            if c3[0] == "#":
                                afterMod = None
                                c3 = c3.replace("#", "")
                                c3 = c3.replace(" ", "")
                                if c3 == "강의":
                                    afterMod = 0
                                    rToMod = True
                                elif c3 == "과제":
                                    afterMod = 1
                                    rToMod = True
                                elif c3 == "일과":
                                    afterMod = 2
                                    rToMod = True

                            if rToMod == True:
                                # 본 시간표에 수정
                                todoList[transIndex][cIndex] = afterMod

                            else:
                                infoText = '오류: 구성요소 지칭어에 알맞은 접두, 접미어가 아닙니다.'

                        elif c2 == "-서브태그":
                            cIndex = 7
                            if todoList[transIndex][cIndex] == None:  # 수정대상이 None값인 경우
                                infoText = '오류: 해당하는 구성요소 지칭어가 없습니다.'
                            if c3[0] == "-":
                                afterMod = c3.replace("-", "")
                                rToMod = True

                            else:
                                infoText = '오류: 구성요소 지칭어를 입력해주세요.'

                        if rToMod == True:
                            # 본 시간표에 수정
                            todoList[transIndex][cIndex] = afterMod

                    elif(foundTodo == False):
                        infoText = '오류: 내용이 일치하는 할 일이 없습니다.'

                #todoList[transIndex]
                #맨 마지막에 수정된 구문이 문법 최종검사
                user_save_check = True
                WriteOnTodoTable(todoList)
                self.setText(NOW_TODO)
                self.addError(infoText)

            # ========== 삭제 ===========
            elif oplist[0] == '/삭제':
                self.resetLine()

                if len(todoList) == 0:
                    infoText = '\n\n오류: 추가한 할 일이 없습니다.'

                elif len(oplist) == 1:
                    reply = QMessageBox.question(
                        self, '경고', '할 일을 전부 삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
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

                tmpStr = ''.join(oplist)[3:]  # '/검색'을 제외하고 공백을 없앤 후 합친 문자열
                if tmpStr == '':  # /검색만 치고 내용을 입력 안 한 케이스
                    self.setText(NOW_TODO)
                    self.addError('오류: 검색할 내용을 1자 이상 입력하세요.')
                    return
                else:
                    # 리스트에 원소가 2개인지 체크해서 2개가 아니면 에러(하이픈이 2개 이상 들어온거)
                    tmpList = tmpStr.split('-')
                    if len(tmpList) > 1:               # '-'뒤에 정수를 입력한 경우
                        searchNum = int(tmpList[1])
                    else:                              # '-' + 정수를 입력하지 않은 경우
                        searchNum = 1

                    searchString = compressWord(tmpList[0])

                    for todo in todoList:
                        count = 0
                        # 공백과 겹치는 문자를 제거한 '할 일' 문자열
                        cmpString = compressWord(todo[0])

                        for cs in cmpString:
                            for ss in searchString:  # 한 글자씩 비교해서 searchNum까지 count 증가시키기
                                if ss == cs:
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
        if (_ == ' ' or _ == ',' or _ == '.' or _ == '!' or _ == '?'):
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
# def pip_install(package):
#     installed = False
#     try:
#         subprocess.check_call(["pip", "install", package])
#         installed = True
#     except Exception as e:
#         print(e)
#         installed = False

#     if not installed:
#         try:
#             subprocess.check_call(["pip3", "install", package])
#         except Exception as e:
#             installed = False
#             print(e)
#             exit(0)


# ========== 메인 ===========


def main():
    # package check - tensorflow
    # try:
    #     import tensorflow as tf
    #     print('tensorflow installed')
    # except Exception as e:
    #     print(e)
    #     pip_install('tensorflow==1.15.*')

    # # package check - PyQt5
    # try:
    #     import PyQt5
    #     print('PyQt5 installed')
    # except Exception as e:
    #     print(e)
    #     pip_install('PyQt5')

    # App Instance
    _ = QApplication(sys.argv)
    app = App()

    global user_save_check
    user_save_check = False

    app.setText(TEXT_MENU)

    # Font
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('C:\Windows\Fonts\D2Coding.ttf')
    _.setFont(QFont('D2Coding'))

    # exit
    sys.exit(_.exec_())


if __name__ == '__main__':
    main()

# EOF
