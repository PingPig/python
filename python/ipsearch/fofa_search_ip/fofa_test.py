import urllib.request 
import string
import re
import subprocess
import linecache
import sys
import base64
import time
def apisearch(emailstr,keystr,targetstr):
    ByteString = targetstr.encode(encoding="utf-8")
    targetstr_Temp = base64.b64encode(ByteString).decode().strip()
    ApiSearchUrl = 'https://fofa.so/api/v1/search/all?email='+emailstr+'&key='+keystr+'&qbase64='+targetstr_Temp+''
    ApiOpen = urllib.request.urlopen(ApiSearchUrl)
    Restring = ApiOpen.read().decode().strip()
    Fofa_iplist = open('Fofa_iplist.txt','w')
    Fofa_ip_data =Fofa_iplist.write(Restring)
    Fofa_iplist.close()
    Format_Fofaip = open('Fofa_iplist.txt')
    Fofaip_read = Format_Fofaip.read()
    Temp_Fofaip = re.sub(r'[[",}{]]*'," ",Fofaip_read)
    Fofa_newip = open('fofa_newip.txt','w')
    Fofa_newip_data = Fofa_newip.write(Temp_Fofaip)
    Fofa_newip.close()
    subp = subprocess.Popen('cat fofa_newip.txt|xargs -n 1 |sed "1,14d" >>fofa_newiplist.txt',shell=True,stdout=subprocess.PIPE)
    num = 1
    while num <=300:
        linecache.getline('fofa_newiplist.txt',num).strip()
        num +=3
if __name__ == "__main__":
    if len(sys.argv)<=2:
        print("Usage:"+" python3"+" fofa_test.py"+" email"+" key"+" zabbix")
    else: 
        apisearch(sys.argv[1],sys.argv[2],sys.argv[3])
