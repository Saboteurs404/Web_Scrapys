import re

douban_html = r""
emails = 'http://blog.csdn.net/make164492212/article/details/51656638'

email_1 = 'zhangshna.Mr@163.com,abc_Wang.dd@sian.com,abc_Wang.dd.cc@sian.com'
res = re.compile(r'[\w]+(\.[\w]+)+@[\w]+(\.[\w+]+)').findall(email_1)
print(res)



