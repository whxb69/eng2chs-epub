import os
import shutil
def format(file):
    #清楚E盘遗留文件
    mime = 'E:mimetype'
    if os.path.exists(mime):
        os.remove(mime)

    oebps = 'E:OEBPS'
    if os.path.exists(oebps):
        shutil.rmtree(oebps)

    meta = 'E:META-INF'
    if os.path.exists(meta):
        shutil.rmtree(meta)

    #清除C盘遗留文件
    oebps = 'C:\\Users\shentong\Downloads\OEBPS'
    if os.path.exists(oebps):
        shutil.rmtree(oebps)

    basedir = 'C:\\Users\shentong\Downloads'
    n = 0
    filedir = basedir + '\\' + str(n) + '_files'
    while os.path.exists(filedir):
        shutil.rmtree(filedir)
        n = n + 1
        filedir = basedir + '\\' + str(n) + '_files'

    m = 0
    htmldir = basedir + '\\' + str(m) + '.html'
    while os.path.exists(htmldir):
        os.remove(htmldir)
        m = m + 1
        htmldir = basedir + '\\' + str(m) + '.html'



    fileformat = os.path.splitext(file)[1]
    filename = os.path.splitext(file)[0]
    newfile = filename + '.zip'
    if fileformat == '.epub':
        shutil.copyfile(file, newfile)
    else:
        print('文件格式错误')

    shutil.unpack_archive(newfile,filename)
    os.remove(file)
    if os.path.exists(newfile):
        os.remove(newfile)
    print('准备工作完成')
