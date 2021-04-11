#-*-coding:utf-8-*-

from PyQt5.QtWidgets import (QApplication,QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser)
from PyQt5.QtGui import (QFontDatabase, QFont)
import sys
import tensorflow as tf

"""
# 전공기초프로젝트1 시간표 생성 프로그램
"""

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('시간표 생성 프로그램')
        self.resize(960, 540)

        grid = QGridLayout()
        self.setLayout(grid)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.tb.setFont

        grid.addWidget(self.tb, 0, 0)
        grid.addWidget(QLineEdit(), 1, 0)
        self.show()

    def clear_screen(self):
        self.tb.clear()

    def append_text(self, t):
        self.tb.setText(t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./D2Coding.ttf')
    app.setFont(QFont('D2Coding'))

    ex.append_text(str(tf.__version__))

    sys.exit(app.exec_())
