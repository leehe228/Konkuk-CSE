#-*-coding:utf-8-*-

import PyQt5
from PyQt5.QtWidgets import (QApplication,QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser)
from PyQt5.QtGui import (QFontDatabase, QFont)
import sys
import subprocess
#import tensorflow as tf

""" TEXT """
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
│  할 일   │ 시작시각 │ 지속시간 │ 종료시각 │        요 일        │   태그   │        서브태그        │"

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

TODO_NUM = 0
NOW_TODO = str(TEXT_TODO_HEADER)

NOW_TABLE = str(TEXT_TABLE)

todoList = list()

"""
# 전공기초프로젝트1 시간표 생성 프로그램
# 3239분반 4조
"""

def WriteOnTodoTable(task):
    global NOW_TODO, TODO_NUM
    global TEXT_TODO_CENTER, TEXT_TODO_BOTTOM

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
        text = h + ':' + m +  "     "
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
        text = h + ':' + m +  "     "
    tempTODO = tempTODO.replace("$R", text)

    # 종료시각
    if (task[2] is None) or (task[4] is None):
        text = "          "
    else:
        sH, sM, rH, rM = task[2], task[3], task[4], task[5]
        m, h = sM + rM, sH + rH
        if m >= 60:
            h =+ m % 60
            m = m // 60
        h, m = str(h), str(m)
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        text = h + ':' + m +  "     "
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
    TODO_NUM += 1

    print(TODO_NUM)
    

def WriteOnTable(task):
    global NOW_TABLE

    sH, sM, rH, rM = task[2], task[3], task[4], task[5]
    eM, eH = sM + rM, sH + rH
    if eM >= 60:
        eH =+ eM % 60
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

    NOW_TABLE = NOW_TABLE.replace(' ┼', ' ├').replace('┼ ', '┤ ').replace(' ├ ', ' │ ')
    NOW_TABLE = NOW_TABLE.replace('│─', '├─').replace('─│', '─┤')


def completeTodo():
    global NOW_TODO
    global TEXT_TODO_BOTTOM
    NOW_TODO = NOW_TODO + '\n' + TEXT_TODO_BOTTOM


def AddTable(task):
    if (task[2] is not None) and (task[4] is not None) and (task[6] is not None):
        WriteOnTable(task)

""" App Class """
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
        self.tb.setText(text)

    # Append Text on TextBrowser
    def appendText(self, text):
        self.tb.append(text)

    # when Enter Pressed
    def opEntered(self):
        opstr = self.opline.text()
        oplist = list(map(str, opstr.split()))

        print(oplist)

        global NOW_TODO, todoList

        # 도움말 함수
        if oplist[0] == '/도움말':
            self.setText(TEXT_HELP)
            self.resetLine()

        elif oplist[0] == '/추가':
            if len(oplist) == 7:
                todoList.append([oplist[1], oplist[2], oplist[3], oplist[4], oplist[5], [oplist[6]], oplist[7]])
                WriteOnTodoTable([oplist[1], oplist[2], oplist[3], oplist[4], oplist[5], [oplist[6]], oplist[7]])
                # completeTodo()
                self.setText(NOW_TODO)

        # Exception
        else:
            self.setText('오류: 인식할 수 없는 명령어입니다.')

    def resetLine(self):
        self.opline.setText('')



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

""" package check """
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