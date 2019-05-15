# eng2chs-epub
将epub电子书格式进行拆解<br>
利用Chrome浏览器的翻译插件(谷歌翻译)翻译epub格式电子书的内容<br>
go.py为主函数 其他为数据抓取和格式文件格式调整函数<br>
在go.py的中的epubfile列表中添加需要翻译的epub文件地址，最好将文件放在E盘根目录下<br>

### 需要将chromedriver添加到Chrome程序根目录下,并将该路径添加进环境变量
chromedriver与chrome的的对应版本<br>
>https://blog.csdn.net/cz9025/article/details/70160273

### 需将程序中所有basedir变量改为Chrome保存文件的路径
