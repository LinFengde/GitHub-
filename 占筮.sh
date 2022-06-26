#！/bin/bash
a=49; # 用五十根蓍草，先抽去一根，象征太极，始终不用。所以总共用得上的是a=49根蓍草。
function zhanshi(){
    b=$[$RANDOM%$[$1-1]+1]; # 剩下的四十九根信手分成两份，象征两仪，左边代表天，右边代表地，左边代表阳，右边代表阴。b表示左手的数量。（[$1-1]是由于RANDOM函数的特性，取值总是在0~x-1，+1是为了保证取到的随机数不为0）
    c=$[$1-$b-1]; #从右边抽出一根放在下方，代表三才中的人，或代表自己，或代表问卦者。（所以这时候右手的数量）
    d=$[$b%4]; # 将左边的蓍草四根一组进行分组，最后的余数等于四或小于四时，放在下边代表“人”的那一根蓍草左半部。四根一组象征四季，余数象征闰月。
    if [ $d == 0 ] ;then # 如果余数为0，则判定余数为4
        d=4;
    fi
    e=$[$c%4]; # 用同样的方法将右边代表“地”的蓍草，四根一组分组，余数等于或小于四时，将其放在下边代表“人”的蓍草的右半部
    if [ $e == 0 ];then # # 如果余数为0，则判定余数为4
        e=4;
    fi
    f=$[$d+$e+1]; # 将下方的蓍草收拢在一起，得到的根数不是九根就是五根
    g=$[$b+$c-$f+1]; # 同时收拢上边剩余的四十或四十四根蓍草
    echo $g;
}
# 连续经过三次变化
h=$(zhanshi $(zhanshi $(zhanshi $a)))
i=$(zhanshi $(zhanshi $(zhanshi $a)))
j=$(zhanshi $(zhanshi $(zhanshi $a)))
# 分析三次变化的情况
case $h in 
24)
echo "第一爻:老阴"
;;
28)
echo "第一爻:少阳"
;;
32)
echo "第一爻:少阴"
;;
36)
echo "第一爻:老阳"
;;
esac

case $i in
24)
echo "第二爻:老阴"
;;
28)
echo "第二爻:少阳"
;;
32)
echo "第二爻:少阴"
;;
36)
echo "第二爻:老阳"
;;
esac

case $j in
24)
echo "第三爻:老阴"
;;
28)
echo "第三爻:少阳"
;;
32)
echo "第三爻:少阴"
;;
36)
echo "第三爻:老阳"
;;
esac
