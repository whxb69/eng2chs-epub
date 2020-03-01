import zipfile, os
import shutil

#遍历目录 将文件加入列表
def get_zip_file(input_path,result):
    # print(input_path)
    files = os.listdir(input_path)
    for file_ in files:
        if os.path.isdir(input_path + '/' + file_):
            get_zip_file(input_path + '/' + file_, result)
        else:
            result.append(input_path + '/' + file_)
    return result

#打包全部文件
def zip_path(oebps_path, meta_path,output_path,output_name):

    # print(output_path + '\\' + output_name)
    f = zipfile.ZipFile((output_path + '\\' + output_name)[3:],'w',zipfile.ZIP_DEFLATED)
    filelists1 = []
    filelists2 = []
    files1 = get_zip_file(oebps_path,filelists1)
    files2 = get_zip_file(meta_path,filelists2)
    files = files1 + files2
    files.append('E:/mimetype')
    print(files)
    for file_ in files:
        # print(file)
        f.write(file_)
    f.close()
    epub = output_path+r"/"+output_name
    return epub

def backtoepub(rootdir):
    #移动文件
    oldoebps = rootdir + '\\' + 'OEBPS'
    newoebps = 'E:/' + 'OEBPS'
    shutil.copytree(oldoebps, newoebps)

    oldMETA = rootdir + '\\' + 'META-INF'
    newMETA = 'E:/' + 'META-INF'
    shutil.copytree(oldMETA, newMETA)

    oldmine = rootdir + '\\' + 'mimetype'
    newmine = 'E:/' + 'mimetype'
    shutil.copy(oldmine, newmine)

    temp = rootdir.split('\\')
    input_path = [newMETA,newoebps]
    # print(temp[0] + '.zip')
    epub = zip_path(newoebps ,newMETA ,'E:',temp[0] + '.zip')
    newepub = epub.split('.')[0] + '.epub'
    os.renames('E' + epub[4:],'E' + newepub[4:])
