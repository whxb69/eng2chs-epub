import win32api
from selenium import webdriver
import os
import win32con
import time
from html2xhtml import toxhtml
import shutil
from backtofuture import backtoepub
from getready import format

epubfile = ['E:rucker-postsingular.epub']

for epub in epubfile:
    filename = os.path.splitext(epub)[0]
    format(epub)

    rootdir = filename + '\\' + 'OEBPS'
    print(rootdir)
    temp = rootdir.split('\\')
    print(temp)
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    urls = []       #待操作文件列表
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        # print(path)
        if os.path.isfile(path) and path[-6:] == '.xhtml':
            # os.renames(path,path[:-6] + '.html')
            urls.append(path)

    names = {}
    keyboard = {'0':0x30,'1':0x31,'2':0x32,
                '3':0x33,'4':0x34,'5':0x35,
                '6':0x36,'7':0x37,'8':0x38,'9':0x39}

    for (j,url) in enumerate(urls):
        os.renames(url, url[:-6] + '.html')
        name = url.split('\\')[-1]
        names[j] = name
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(url[:-6] + '.html')

        win32api.SetCursorPos([1000, 150])
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)     #右键菜单
        time.sleep(1)

        win32api.SetCursorPos([1025, 320])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)       #点击翻译选项
        time.sleep(2)

        for upanddown in range(20):                                                                              #上下滚动网页 保证翻译效果
            win32api.keybd_event(0x22, 0, 0, 0)
            time.sleep(2)
            win32api.keybd_event(0x21, 0, 0, 0)
            time.sleep(2)



        win32api.SetCursorPos([1000, 150])
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)     #右键菜单
        time.sleep(1)

        #单击命名框
        win32api.SetCursorPos([1025, 250])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击另存为选项
        time.sleep(1)

        #输入对应标号
        cur_name = ''
        if j < 10:
            win32api.keybd_event(keyboard[str(j)], 0, 0, 0)
            cur_name = str(j)
            time.sleep(1)

        elif j < 100:
            j1 = int(j / 10)
            j2 = int(j % 10)
            win32api.keybd_event(keyboard[str(j1)], 0, 0, 0)
            time.sleep(1)
            win32api.keybd_event(keyboard[str(j2)], 0, 0, 0)
            cur_name = str(j1) + str(j2)
            time.sleep(1)
        else:
            j1 = int(j / 100)
            j2 = int((j / 10) % 10)
            j3 = int(j % 10)
            win32api.keybd_event(keyboard[str(j1)], 0, 0, 0)
            time.sleep(1)
            win32api.keybd_event(keyboard[str(j2)], 0, 0, 0)
            time.sleep(1)
            win32api.keybd_event(keyboard[str(j3)], 0, 0, 0)
            cur_name = str(j1) + str(j2) + str(j3)
            time.sleep(1)


        win32api.SetCursorPos([500, 420])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)       #点击保存
        time.sleep(5)

        #翻译并保存完成
        basedir = 'C:\\Users\shentong\Downloads\\'      #保存地址
        print(names)
        oldfile = rootdir + '\\' + names[int(cur_name)]
        print(oldfile,type(oldfile))
        oldfile = str(oldfile).split('.')[0] + '.html'

        os.remove(oldfile)
        newname = basedir + rootdir.split('\\')[-1] + '\\' + names[int(cur_name)][:-5]
        isExists = os.path.exists(basedir + rootdir.split('\\')[-1])
        # 判断结果
        if not isExists:
            os.makedirs(basedir + rootdir.split('\\')[-1])

        print(cur_name)
        try:
            text = toxhtml(basedir + cur_name + '.html')
        # 解决未知bug chrome浏览器保存网页后可能不存在该文件
        except:
            sparedir = basedir + cur_name + '_files' + '\\' + 'saved_resource.html'
            text = toxhtml(sparedir)

        filename = rootdir + '\\' + names[int(cur_name)][:-5] + 'xhtml'
        with open(filename, 'w', encoding="utf-8") as f:
            try:
                f.write(text)
            except:
                f.write(text.decode('utf-8'))

        olddir = basedir + cur_name + '_files'
        newdir = rootdir + '\\' + cur_name + '_files'
        if os.path.exists(olddir):
            shutil.copytree(olddir, newdir)
        browser.close()

    backtoepub(rootdir[:-6])
print('完成！')

