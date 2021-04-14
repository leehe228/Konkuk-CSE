#-*-coding:utf-8-*-

import PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser)
from PyQt5.QtGui import (QFontDatabase, QFont)
import sys
import subprocess
#import tensorflow as tf

from text_datas import TEXT_HELP, BAR, SPC, TEXT_TODO_HEADER, TEXT_TODO_CENTER, TEXT_TODO_BOTTOM, TEXT_TABLE, TEXT_MENU

THIS_PAGE = 1

NOW_TODO = str(TEXT_TODO_HEADER)

NOW_TABLE = str(TEXT_TABLE)

todoList = list()

"""
# 전공기초프로젝트1 시간표 생성 프로그램
# 3239분반 4조
"""

def WriteOnTodoTable(tasks):
    global NOW_TODO
    global TEXT_TODO_CENTER, TEXT_TODO_BOTTOM

    NOW_TODO = str(TEXT_TODO_HEADER)
    tempTODO = str(TEXT_TODO_CENTER)

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
        tags = ['강의      ', '과제      ', '일과      ']
        tempTODO = tempTODO.replace("$G", tags[task[1]])

        # 서브태그
        if task[7] is None:
            text = "                        "
        else:
            text = task[7] + ' '*(24 - GetFixedLen(task[7]))
        tempTODO = tempTODO.replace("$D", text)

        NOW_TODO = NOW_TODO + '\n' + tempTODO

    completeTodo()


def WriteOnTable(task):
    global NOW_TABLE

    sH, sM, rH, rM = task[2], task[3], task[4], task[5]
    eM, eH = sM + rM, sH + rH
    if eM >= 60:
        eH = + eM % 60
        eM = eM // 60

    # 30분만 지속하는 경우
    if rH == 0 and rM == 30:
        text = task[0] + '─'*(10 - GetFixedLen(task[0]))
    else:
        text = task[0] + ' '*(10 - GetFixedLen(task[0]))

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


def completeTable():
    week = ['M', 'T', 'W', 'H', 'F', 'S', 'U']
    global NOW_TABLE

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


def completeTodo():
    global NOW_TODO
    global TEXT_TODO_BOTTOM
    NOW_TODO = NOW_TODO + '\n' + TEXT_TODO_BOTTOM


def AddTable(tasks):
    for task in tasks:
        if (task[2] is not None) and (task[4] is not None) and (task[6] is not None):
            WriteOnTable(task)


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
        self.tb.setOpenExternalLinks(True)

        # LineEdit
        self.opline = QLineEdit()
        self.opline.setPlaceholderText("명령어: ")
        self.opline.editingFinished.connect(self.opEntered)

        # Add Widget
        grid.addWidget(self.tb, 0, 0)
        grid.addWidget(self.opline, 1, 0)
        self.show()

    # Clear Screen
    def clearScreen(self):
        self.tb.clear()

    # Set Text on TextBrowser
    def setText(self, text):
        self.tb.clear()
        self.tb.setText(text)

    # Append Text on TextBrowser
    def appendText(self, text):
        self.tb.append(text)

    # when Enter Pressed
    def opEntered(self):

        global NOW_TODO, todoList

        opstr = self.opline.text()
        oplist = list(map(str, opstr.split()))

        # 도움말 함수
        if oplist is None:
            pass
        elif oplist[0] == '/도움말':
            self.setText(TEXT_HELP)
            self.resetLine()

        elif oplist[0] == '/추가':
            todoList.append([oplist[1], int(oplist[2]), int(oplist[3]), int(oplist[4]), int(oplist[5]), int(oplist[6]), [oplist[7]], oplist[8]])
            WriteOnTodoTable(todoList)
            self.setText(NOW_TODO)

        elif oplist[0] == '//':
            pass

        elif oplist[0] == '/입력완료':
            AddTable(todoList)
            completeTable()
            self.setText(NOW_TABLE)

        elif oplist[0] == '/수정':
            pass

        elif oplist[0] == '/삭제':
            pass

        elif oplist[0] == '/검색':
            pass

        elif oplist[0] == '/종료':
            pass

        # Exception
        else:
            self.setText('오류: 인식할 수 없는 명령어입니다.')

        self.opline.clear()
        oplist = None


    def resetLine(self):
        self.opline.clear()

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


def pip_install(package):
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


if __name__ == '__main__':
    # package check - tensorflow
    try:
        # import tensorflow as tf
        print('tensorflow installed')
    except Exception as e:
        print(e)
        pip_install('tensorflow==2.4.1')

    # package check - PyQt5
    try:
        import PyQt5
        print('PyQt5 installed')
    except Exception as e:
        print(e)
        pip_install('PyQt5')

    # App Instance
    _ = QApplication(sys.argv)
    app = App()

    # Font
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./D2Coding.ttf')
    _.setFont(QFont('D2Coding'))

    # exit
    sys.exit(_.exec_())

# EOF
