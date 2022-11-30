import random
import re
import requests
url = '4.52vpn.club'
#注册界面的请求链接
#f"字符串{变量}":在字符串里面的括号内输入
RegisterUrl=f"http://{url}/auth/register"
#登陆页面的请求链接
LoginUrl=f"http://{url}/auth/login"
#tok
tok="b=3"
#生成一个随机数作为邮箱
EmailNum=random.randint(100000000, 999999999)
email=(str(EmailNum) + "@lc.com")
print (email)
#设置登陆密码
passwd='LC20030308'
print (passwd)
#设置链接方式
#requests.session(): 保持连接(保留cookie)
http=requests.session()
#注册信息的内容
RegisterUrlData={"email": str(EmailNum) + "@lc.com",
            "name": "00000",
            "passwd": str(passwd),
            "repasswd": str(passwd),
            "geetest_challenge": "98dce83da57b0395e163467c9dae521b1f",
            "geetest_validate": "bebe713_e80_222ebc4a0",
            "geetest_seccode": "bebe713_e80_222ebc4a0|jordan"}
#把注册信息的内容写入到注册的请求网站
#post:以post形式请求
#json:以json格式解析
RegisterBack=http.post((RegisterUrl), RegisterUrlData).json()
#输出注册成功反馈包的内容
print(RegisterBack)
#设置登陆信息
LoginData={"email": str(EmailNum) + "@lc.com",
            "passwd": passwd, "code": ""}
#把登陆信息写入到登陆的请求网站
LoginBack=http.post((LoginUrl), LoginData).json()["msg"]
#以get格式请求
#./text:
http_back = http.get(f"https://{url}/user")
#re.search(内容)group(数字):全文查找到匹配的内容，并提取第几项
#网站是正则表达式(我暂时理解不了)
DYurl = re.search(f"https://[\\w./?=&]+{tok}[\\w=&]*", http_back).group(0)
print (DYurl)
