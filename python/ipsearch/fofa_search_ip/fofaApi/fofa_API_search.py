import urllib.request 
# from urllib.parse import quote
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
    Temp_dict = re.sub(r'[}{]','',Restring)
    Temp_Format = Temp_dict.split('"results":')[1]
    for_list = eval(Temp_Format)
    Fofa_iplist = open('/root/桌面/python/fofaApi/Fofa_iplist.txt','w')
    for i in range(len(for_list)):
        for j in range(0,1):
            IPlist_fofa = for_list[i][j]
            Fofa_ip_Data = Fofa_iplist.write(IPlist_fofa)
    Fofa_iplist.close()
if __name__ == "__main__":
        apisearch('xxxxxx@sina.com','xxxxxx','xxxx')
