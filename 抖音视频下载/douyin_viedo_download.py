import requests
import re
from urllib import parse
#想要爬的抖音视频链接
url = input('请输入你想要下载的视频链接：')
video_name=input('请输入你想要的视频文件名(不能为空):')
#请求头参数
headers = {
    #'Accept': '*/*',
    #'Accept-Encoding': 'identity;q=1, *;q=0',
    #'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #'Connection': 'keep-alive',
    #'Host': 'v26-web.douyinvod.com',
    #'Origin': 'https://www.douyin.com',
    #'Range': 'bytes=0-',
    #'Referer': 'https://www.douyin.com/',
    #'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    #'sec-ch-ua-mobile': '?0',
    #'sec-ch-ua-platform': '"Windows"',
    #'Sec-Fetch-Dest': 'video',
    #'Sec-Fetch-Mode': 'cors',
    #'Sec-Fetch-Site': 'ross-site',
    'cookie':'douyin.com; ttwid=1%7CanmsunwoFcFqtWUSolThiUrnRLACXqVD1KJ_nW4To7Y%7C1673934963%7Cead284800d8cb243693bddcd266807b3c2e26077ce6bdf55284f394f92dce92c; passport_csrf_token=23f192005d822677dd320bb00b244862; passport_csrf_token_default=23f192005d822677dd320bb00b244862; s_v_web_id=verify_lcztnq6p_je4mwVeL_P4XV_4beR_8nAu_ZskKsn99Hl3z; ttcid=ad8f6a59f4a84bd48faa1347e3e3aaaf36; n_mh=_hjMo0XeYAL0xHOj-0NKgwD0Gpufc99xoEXxoEB_q_E; _tea_utm_cache_2018=undefined; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1674539827058%2C%22type%22%3A1%7D; store-region=cn-fj; store-region-src=uid; download_guide=%223%2F20230117%22; passport_auth_status=57647748928d6fdae8c66ae3f1c38931%2C5df21617c5e1b0b086696a26a97ed7a4; passport_auth_status_ss=57647748928d6fdae8c66ae3f1c38931%2C5df21617c5e1b0b086696a26a97ed7a4; LOGIN_STATUS=1; passport_assist_user=CjyceeECG1WhJnY6cvQZ40f2EDABn27CF7Aq3zM_d2s5I_cZDeylUMtd3PpUrQM7qVYHVzcUmI5-HMM6Q_4aSAo8lZMrmTpWZxi6ZcWCg04IreLUx5SBSxUojTWok8vRG6MNRULvUKpg1Fe6zXuH_GQiE3n0SgDVIHI3Tlx3EK7qpg0Yia_WVCIBAz2pPXk%3D; sso_uid_tt=0c9dae0c75f40970bbd9f1e92d9b38a4; sso_uid_tt_ss=0c9dae0c75f40970bbd9f1e92d9b38a4; toutiao_sso_user=bae15444dd53c7a766edbf0845b45515; toutiao_sso_user_ss=bae15444dd53c7a766edbf0845b45515; sid_ucp_sso_v1=1.0.0-KDg5YzA1NzliZDJiOTEzZTc2NWI3YWRiOWE3ZmMyYTI0ZjNjMTY5M2QKHQj76a_soAIQuYibngYY7zEgDDDRxurQBTgCQO8HGgJobCIgYmFlMTU0NDRkZDUzYzdhNzY2ZWRiZjA4NDViNDU1MTU; ssid_ucp_sso_v1=1.0.0-KDg5YzA1NzliZDJiOTEzZTc2NWI3YWRiOWE3ZmMyYTI0ZjNjMTY5M2QKHQj76a_soAIQuYibngYY7zEgDDDRxurQBTgCQO8HGgJobCIgYmFlMTU0NDRkZDUzYzdhNzY2ZWRiZjA4NDViNDU1MTU; odin_tt=3e3d88b7d299da2fc7260944403127225fea936510df7d6fc8b5d2adcab64767d063099ae0975d9df1b836b91b8d52e5; uid_tt=c3ae9e5e70fa9ad9142b5c7637c4bdd4; uid_tt_ss=c3ae9e5e70fa9ad9142b5c7637c4bdd4; sid_tt=95c6258f0294c055d577f04cc74fe356; sessionid=95c6258f0294c055d577f04cc74fe356; sessionid_ss=95c6258f0294c055d577f04cc74fe356; sid_guard=95c6258f0294c055d577f04cc74fe356%7C1673970748%7C5183997%7CSat%2C+18-Mar-2023+15%3A52%3A25+GMT; sid_ucp_v1=1.0.0-KDBjZWQ0OTBmY2U3YWE0MGMzNzBmYzVmMWI3MjZmMzFkYmQ5ZmFmYzAKFwj76a_soAIQvIibngYY7zEgDDgCQO8HGgJsZiIgOTVjNjI1OGYwMjk0YzA1NWQ1NzdmMDRjYzc0ZmUzNTY; ssid_ucp_v1=1.0.0-KDBjZWQ0OTBmY2U3YWE0MGMzNzBmYzVmMWI3MjZmMzFkYmQ5ZmFmYzAKFwj76a_soAIQvIibngYY7zEgDDgCQO8HGgJsZiIgOTVjNjI1OGYwMjk0YzA1NWQ1NzdmMDRjYzc0ZmUzNTY; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA_vsDjhi4BFZk7Mm9KyPzwtA4ZyftQ_vy-vf4EVJeyhI%2F1674057600000%2F0%2F1674034639542%2F0%22; tt_scid=Y5lL-PllDAhAOu4Ki3wVXlD8W3XaZs7NglH0eHe1BIyIOv7HN3f76QUpe0eLXGik112e; __ac_nonce=063c8095500486e8fa5e9; __ac_signature=_02B4Z6wo00f01R8vq8wAAIDAD3FO9k-kUb0fD69AACQGHc2mTHM6fUL9jsSiaEGEJwDRJQx68RgyISzIJp2esQZClK5OXL82rSCYGoOhqnxHv.LDlD3yRh7PT7oNcRAJfnaLQGNEv5gTkKyV64; strategyABtestKey=%221674053975.7%22; home_can_add_dy_2_desktop=%221%22; msToken=h5zffb_eJ1v4qu0riftd2hLcmkSbOJfVMHfgeU6t9IEc1xwcsosiK3_gViawyxZM7pq7e9JknToCJ0v8gP5vsTS9PFHFlRaMWB6vbLbdl76nM4CGEEyS4HMxVv5SNCs=; msToken=SZj-DFQqG01zsA4DJWaK_jy1H_v47eNZaQ-49XdetwyftWzpAQhTdQ4O-ymSRl77N-CjLINAJP39jWXkBmENy1FXTW5Pl3ogiyidhRR7pJKLdsKzV3QO7g==; passport_fe_beating_status=false',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55'
}
#向链接发出get请求
response = requests.get(url=url, headers=headers)
#print(response.text)

#在请求包的源码中提取视频标题(不稳定)
#title=re.findall('<title data-react-helmet="true">(.*?)</title>',response.text)[0]
#print(title)

#提取视频链接
video_url=re.findall('%22%2C%22playAddr%22%3A%5B%7B%22src%22%3A%22(.*?)%22%7D%2C%7B%22src%22%3A%22%2F%2F',response.text)
video_url=str(video_url)
#链接转码
new_video_url = 'https:'+parse.unquote(video_url)
#print(new_video_url)

#视频链接再次处理（去括号，引号）
a = new_video_url.replace('[', '')
b = a.replace(']','')
true_video_url=re.sub("'", "", b)
print(true_video_url)

video_content=requests.get(url=true_video_url,headers=headers).content
with open(video_name+'.mp4',mode='wb') as f:
    f.write(video_content)




















#https://v26-web.douyinvod.com/2fd28634b7b67202c3668613bc7cb50f/63ccc82e/video/tos/cn/tos-cn-ve-15c001-alinc2/oEfe9EvjxASTAW9QhLcMH98BCoENUzXUAWJgIz


# https://v26-web.douyinvod.com/2402d5d07e6036c94b8f009cfd1061a3/63ccb803/video/tos/cn/tos-cn-ve-15/oc6ANu8xYhnP6tAA9kfgbxDZjJRf93dACK1MnB/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1688&bt=1688&cs=0&ds=3&ft=bvTKJbQQqUGXf_.Zao0OqY8hFgpiRm0j~jKJittZ1N0P3-A&mime_type=video_mp4&qs=0&rc=OGZoZDc6aTw0MzdkN2lpNEBpanB3OmU6ZnhmaTMzNGkzM0BhYjI2Xy4uXzExLzAuLy5gYSMxMy9fcjRnci9gLS1kLS9zcw%3D%3D&l=20230120121342982EF30697209F3FD856&btag=8000

