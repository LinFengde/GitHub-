#！/bin/bash
j=49;
function zhanshi(){
    a=$[$RANDOM%$[$1-1]+1];
    b=$[$1-$a-1];
    c=$[$a%4];
    if [ $c == 0 ] ;then
        c=4;
    fi
    d=$[$b%4];
    if [ $d == 0 ];then
        d=4;
    fi
    e=$[$c+$d+1];
    f=$[$a+$b-$e+1];
    echo $f
}

g=$(zhanshi $(zhanshi $(zhanshi $j)))
h=$(zhanshi $(zhanshi $(zhanshi $j)))
i=$(zhanshi $(zhanshi $(zhanshi $j)))

case $g in
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

case $h in
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

case $i in
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




