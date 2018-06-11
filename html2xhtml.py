from urllib import parse, request

def toxhtml(file):
    params = parse.urlencode({'tablength': 4,
                              'linelength': 100,
                              'output-charset': 'UTF-8'})
    url = 'http://www.it.uc3m.es/jaf/cgi-bin/html2xhtml.cgi?' + params
    headers = {"Content-type": "text/html",
               "Accept": "application/xhtml+xml"}
    # headers['Host'] = 'httpbin.org'
    in_file = open(file, 'r', encoding='utf-8')
    data = in_file.read().encode('utf-8')

    params = parse.urlencode({'tablength': 4,
                              'linelength': 100,
                              'output-charset': 'UTF-8'})
    # data参数如果要传必须传bytes（字节流）类型的，如果是一个字典，先用urllib.parse.urlencode()编码。
    requests = request.Request(url=url, data=data, headers=headers, method='POST')

    response = request.urlopen(requests)
    text = response.read().decode('utf-8', 'ignore').replace(u'\xa9', u'')

    print(text)
    return text