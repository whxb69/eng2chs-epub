# eng2chs-epub
将epub电子书格式进行拆解<br>
利用Chrome浏览器的翻译插件(谷歌翻译)翻译epub格式电子书的内容<br>
go.py为主函数 其他为数据抓取和格式文件格式调整函数<br>
在go.py的中的epubfile列表中添加需要翻译的epub文件地址，最好将文件放在E盘根目录下<br>

**需要将chromedriver添加到Chrome程序根目录下,并将该路径添加进环境变量
chromedriver与chrome的的对应版本**<br>
>https://blog.csdn.net/cz9025/article/details/70160273

**需将程序中所有basedir变量改为Chrome保存文件的路径**

## 操作流程
- 读取待处理文件目录
- 准备阶段
  - 清理失败残留文件或临时文件
  - epub复制生成zip
  - 解压zip然后删除zip
  - 更改xhtml文件名
    - 文件类型改为html
      - 否则无法翻译
    - 文件名改为数字标号
    - 建立标号和文件名字典
- 翻译
  - 调用selenium模拟浏览器
  - 调用win32api操作键盘鼠标
  - 调用网站api将html转回xhtml
    - 发送post请求
    - 包含内容和格式等参数
  - 用原文件名保存xhtml
- 重新打包zip还原epub
  - 遍历目录下文件加入list
  - 打包list内文件为zip
  - zip重命名为epub
