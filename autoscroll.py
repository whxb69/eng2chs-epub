#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import win32api
import win32con
import chardet
import time
from lxml import etree
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui import *
import sys

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.getfile)
        self.pushButton_2.clicked.connect(self.main)

    def getfile(self):
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "",
                                                         "All File(*.*)")
        self.html =  FileName
        self.label.setText(self.html)

    def main(self):
    # htmls = [os.path.abspath(file) for file in os.listdir() if os.path.splitext(file)[1] == '.html']


    # for html in htmls:
        html = self.html
        driver = webdriver.Chrome()
        # url = 'http://www.ophiuchi.net/'
        driver.get(html)
        h = []
        cur = driver.execute_script("return document.documentElement.scrollHeight")
        driver.maximize_window()
        time.sleep(2)
        print(cur)
        win32api.SetCursorPos([1500, 300])
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)  # 右键菜单
        time.sleep(1)

        win32api.keybd_event(84, 0, 0, 0)  # 点击翻译选项
        time.sleep(2)
        while h.count(cur) < 2:
            win32api.keybd_event(34, 0, 0, 0)
            time.sleep(2)
            cur = driver.execute_script("return document.documentElement.scrollTop")
            print(cur)
            h.append(cur)

        page = driver.page_source
        page = etree.HTML(page)
        page = etree.tostring(page)
        newhtml = os.path.splitext(html)[0] + '_chs.html'
        # chardet.detect(page)

        with open(newhtml,'w') as f:
            f.write(str(page,encoding='utf-8'))
        driver.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())

