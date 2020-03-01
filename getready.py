import os
import shutil
def format_(filename):
    #清除工作目录遗留文件（失败残留或临时文件）
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



    fileformat = os.path.splitext(filename)[1]
    filename = os.path.splitext(filename)[0]
    newfile = filename + '.zip'
    #epub复制生成zip文件
    if fileformat == '.epub':
        shutil.copyfile(filename, newfile)
    else:
        print('文件格式错误')
    #zip解压然后删除zip
    shutil.unpack_archive(newfile,filename)
    os.remove(filename)#这句可能有问题 remove文件夹会报OSError
    if os.path.exists(newfile):
        os.remove(newfile)
    print('准备工作完成')
