from ast import parse
import re
import requests

title=input('请输入你要保存的文件名:')
url='https://cn.bing.com/?mkt=zh-CN'
headers = {
    'Referer': 'https://cn.bing.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'
}
response = requests.get(url=url, headers=headers)
#print(response.text)

img_url=re.findall('style="background-image: url(.*?)opacity',response.text)
video_url=str(img_url)
img_url=str(img_url)
#print(img_url) 
a = img_url.replace('[', '')
b = a.replace(']','')
c = b.replace('(','')
d = c.replace(')','')
e = d.replace(';','')
true_img_url=re.sub("'", "", e)
print(true_img_url)

img_content=requests.get(url=true_img_url,headers=headers).content
with open(title+'.jpg',mode='wb') as f:
    f.write(img_content)
