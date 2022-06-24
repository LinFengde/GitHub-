#！/bin/bash
function zhanshi(){
    a=$[$RANDOM%$[$1-1]+1];
    b=$[48-$a];
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
}

g=$(zhouyi $(zhouyi $(zhouyi 49)))
h=$(zhouyi $(zhouyi $(zhouyi 49)))
i=$(zhouyi $(zhouyi $(zhouyi 49)))

case $g in 24
echo 
