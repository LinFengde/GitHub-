import random
from re import I
#用五十根蓍草，先抽去一根，象征太极，始终不用。所以总共用得上的是a=49根蓍草。
def zhanshi(a=49):
#剩下的四十九根信手分成两份，象征两仪，左边代表天，右边代表地，左边代表阳，右边代表阴。b表示左手的数量。
    b=random.randint(1,a)
    c=a-b-1
    d=b%4
    if d==0:
        d=4
    e=c%4
    if e==0:
        e=4
    f=d+e+1
    g=b+c-f+1
    return g
h=zhanshi(zhanshi(zhanshi()))
i=zhanshi(zhanshi(zhanshi()))
j=zhanshi(zhanshi(zhanshi()))
if h==24:
    print ("第一爻:老阴")
elif    h==28:
    print ("第一爻:少阳")
elif    h==32:
    print ("第一爻:少阴")
elif    h==36:
    print ("第一爻:老阳")

if i==24:
    print ("第二爻:老阴")
elif    i==28:
    print ("第二爻:少阳")
elif    i==32:
    print ("第二爻:少阴")
elif    i==36:
    print ("第二爻:老阳")

if j==24:
    print ("第三爻:老阴")
elif    j==28:
    print ("第三爻:少阳")
elif    j==32:
    print ("第三爻:少阴")
elif    j==36:
    print ("第三爻:老阳")

if h==24 and i==24 and j==24:
    print ("卦象:坤卦")
if h==24 and i==24 and j==28:
    print ("卦象:师卦")
if h==24 and i==24 and j==32:
    print ("卦象:复卦")
if h==24 and i==24 and j==36:
    print ("卦象:临卦")
if h==24 and i==28 and j==24:
    print ("卦象:豫卦")
if h==24 and i==28 and j==28:
    print ("卦象:解卦")
if h==24 and i==28 and j==32:
    print ("卦象:震卦")
if h==24 and i==28 and j==36:
    print ("卦象:归妹卦")
if h==24 and i==32 and j==24:
    print ("卦象:谦卦")
if h==24 and i==32 and j==28:
    print ("卦象:升卦")
if h==24 and i==32 and j==32:
    print ("卦象:明夷卦")
if h==24 and i==32 and j==36:
    print ("卦象:泰卦")
if h==24 and i==36 and j==24:
    print ("卦象:小过卦")
if h==24 and i==36 and j==28:
    print ("卦象:恒卦")
if h==24 and i==36 and j==32:
    print ("卦象:丰卦")
if h==24 and i==36 and j==36:
    print ("卦象:大壮卦")
if h==28 and i==24 and j==24:
    print ("卦象:剥卦")
if h==28 and i==24 and j==28:
    print ("卦象:蒙卦")
if h==28 and i==24 and j==32:
    print ("卦象:颐卦")
if h==28 and i==24 and j==36:
    print ("卦象:损卦")
if h==28 and i==28 and j==24:
    print ("卦象:晋卦")
if h==28 and i==28 and j==28:
    print ("卦象:未济卦")
if h==28 and i==28 and j==32:
    print ("卦象:噬嗑卦")
if h==28 and i==28 and j==36:
    print ("卦象:睽卦")
if h==28 and i==32 and j==24:
    print ("卦象:艮卦")
if h==28 and i==32 and j==28:
    print ("卦象:蛊卦")
if h==28 and i==32 and j==32:
    print ("卦象:贲卦")
if h==28 and i==32 and j==36:
    print ("卦象:大畜卦")
if h==28 and i==36 and j==24:
    print ("卦象:旅卦")
if h==28 and i==36 and j==28:
    print ("卦象:鼎卦")
if h==28 and i==36 and j==32:
    print ("卦象:离卦")
if h==28 and i==36 and j==36:
    print ("卦象:大有卦")
