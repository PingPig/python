#!/bin/bash
#iplist=$(cat fofa_api.txt|sed 's/\[//g;s/\]//g;s/\}//g;s/{//g;s/"//g')
for ((i=1;i<=300;i=$i+3))
do
	echo $(cat fofa_api.txt |sed 's/\[//g;s/\]//g;s/\}//g;s/{//g;s/"//g'|cut -d \, -f $i)
done	
