import win32api
from selenium import webdriver
import os
import win32con
import time
from html2xhtml import toxhtml
import shutil
from backtofuture import backtoepub
from getready import format_

epubfile = ['E:rucker-postsingular.epub']

#遍历epub列表
for epub in epubfile:
    filename = os.path.splitext(epub)[0]
    #调用getready中函数 
    format_(epub)

    rootdir = filename + '\\' + 'OEBPS'     #主要操作目录
    print(rootdir)
    temp = rootdir.split('\\')
    print(temp)
    flist = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    urls = []       #待操作xhtml文件列表
    for i in range(0,len(flist)):
        path = os.path.join(rootdir,flist[i])
        # print(path)
        if os.path.isfile(path) and os.path.splitext(path)[1] == '.xhtml':
            # os.renames(path,path[:-6] + '.html')
            urls.append(path)

    names = {}
    #win32api字典 
    keyboard = {'0':0x30,'1':0x31,'2':0x32,
                '3':0x33,'4':0x34,'5':0x35,
                '6':0x36,'7':0x37,'8':0x38,'9':0x39}

    for (j,url) in enumerate(urls):
        #文件名统一改为标号 并将原名记入字典
        newname = os.path.splitext(url)[0] + '.html'
        os.renames(url, newname)
        name = url.split('\\')[-1]
        names[j] = name
        
        #模拟浏览器打开待翻译文件
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(newname)
        
        #调用win32api进行鼠标键盘操作
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
        oldfile = os.path.splitext(str(oldfile))[0] + '.html'

        os.remove(oldfile)
        newname = basedir + rootdir.split('\\')[-1] + '\\' + os.path.splitext(names[int(cur_name)])[0]
        isExists = os.path.exists(basedir + rootdir.split('\\')[-1])
        # 判断结果 目标文件夹是否存在
        if not isExists:
            os.makedirs(basedir + rootdir.split('\\')[-1])

        print(cur_name)
        #将html转回xhtml
        try:
            text = toxhtml(basedir + cur_name + '.html')
        # 解决未知bug chrome浏览器保存网页后可能不存在该文件
        except:
            sparedir = basedir + cur_name + '_files' + '\\' + 'saved_resource.html'
            text = toxhtml(sparedir)

        #使用原文件名保存xhtml文件
        filename = rootdir + '\\' + os.path.splitext(names[int(cur_name)])[0] + '.xhtml'
        with open(filename, 'w', encoding="utf-8") as f:
            try:
                f.write(text)
            except:
                f.write(text.decode('utf-8'))

        #统一转移文件目录
        olddir = basedir + cur_name + '_files'
        newdir = rootdir + '\\' + cur_name + '_files'
        if os.path.exists(olddir):
            shutil.copytree(olddir, newdir)
        browser.close()
    #重新打包zip
    backtoepub(rootdir[:-6])
print('完成！')

