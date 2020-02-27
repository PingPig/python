import os
b = os.system('for ((i=1;i<=300;i=$i+3))do      $(cat /root/桌面/python/fofaApi/fofa_newip.txt|xargs -n 1|sed "1,14d"| head -n $i)done')
print(b)