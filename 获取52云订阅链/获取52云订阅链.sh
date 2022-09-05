#!/bin/bash
#注册界面的请求链接
RegisterUrl=http://2.52vpn.club/auth/register
#登陆页面的请求链接
LoginUrl=http://2.52vpn.club/auth/login
#tok
tok="b=3"
#随机生成一个10位数的邮箱
email=$(tr -dc 0-9 < /dev/urandom | head -c10)
echo $email@lc.com
#验证码
vcode="&geetest_challenge=d1fe173d08e959397adf34b1d77e88d7f7&geetest_validate=75775555755555e84_555557757550_755555775579b13&geetest_seccode=75775555755555e84_555557757550_755555775579b13|jordan"
#设置密码
password=LC20030308
#输出密码
echo $password
#配置curl的运行环境为ipv4
curl_path="curl -4 -s"
#注册
echo -e `$curl_path "$RegisterUrl" -X POST -d "email=$email%40qs.com&name=zido&passwd=$password&repasswd=$password$vcode" -c cookie`
#登陆
echo -e `$curl_path -b cookie "$LoginUrl" -X POST -d "email=$email%40qs.com&passwd=$password&code" -c cookie`
#获取订阅链并输出到add.txt
#sed:编辑信息
$curl_path -b cookie "http://2.52vpn.club/user##" | sed 's/"/\n/g' | grep "$tok" | head -n 1 > add.txt
#查看这个文件
cat add.txt