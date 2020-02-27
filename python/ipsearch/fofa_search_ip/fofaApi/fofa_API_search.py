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
        #key
        #email
        #qbase64
    ByteString = targetstr.encode(encoding="utf-8")
    targetstr_Temp = base64.b64encode(ByteString).decode().strip()
    ApiSearchUrl = 'https://fofa.so/api/v1/search/all?email='+emailstr+'&key='+keystr+'&qbase64='+targetstr_Temp+''
        # s = quote(url,safe=string.printable)
    ApiOpen = urllib.request.urlopen(ApiSearchUrl)
    Restring = ApiOpen.read().decode().strip()
    Temp_dict = re.sub(r'[}{]','',Restring)
    Temp_Format = Temp_dict.split('"results":')[1]
    for_list = eval(Temp_Format)
    Fofa_iplist = open('/root/桌面/python/fofaApi/Fofa_iplist.txt','w')
    for i in range(len(for_list)):
        for j in range(0,1):
            # print(for_list[i][j])
            IPlist_fofa = for_list[i][j]
            Fofa_ip_Data = Fofa_iplist.write(IPlist_fofa)
    Fofa_iplist.close()
    # Fofa_iplist = open('Fofa_iplist.txt','w')
    # Fofa_ip_data =Fofa_iplist.write(Restring)
    # Fofa_iplist.close()
    #     # sup_ip = subprocess.Popen("cat iplist.txt",shell=True,stdout=subprocess.PIPE)
    #     # read_sup_ip = sup_ip.stdout.readline().decode().strip()
    # Format_Fofaip = open('Fofa_iplist.txt')
    # Fofaip_read = Format_Fofaip.read()
    # Temp_Fofaip = re.sub(r'[[",}{]]*'," ",Fofaip_read)
    # Fofa_newip = open('fofa_newip.txt','w')
    # Fofa_newip_data = Fofa_newip.write(Temp_Fofaip)
    # Fofa_newip.close()
    # subp = subprocess.Popen('cat fofa_newip.txt|xargs -n 1 |sed "1,14d" >>fofa_newiplist.txt',shell=True,stdout=subprocess.PIPE)
    #     # f1 = open('fofa_api_iplist.txt')
    # time.sleep(3)
# def inputer():
#     num = 1
#     while num <=300:
#         linecache.getline('fofa_newiplist.txt',num).strip()
#     # FoFa_IPlist = open('FoFa_IPlist.txt','w')
#     # FoFa_IPlist_Data = linecache.getline('fofa_newiplist.txt',num).strip()
#     # FoFa_NewIPlist = FoFa_IPlist.write(FoFa_IPlist_Data)
#         num +=3
if __name__ == "__main__":
    # if len(sys.argv)<=2:
    #     print("Usage:"+" python3"+" fofa_test.py"+" email"+" key"+" zabbix")
    # else: 
        apisearch('1121860875@qq.com','674e75ec57e0857f1b93516d74245841','FortiOS')
        # inputer()
# import base64
# s = 'cisco'
# bytestring = s.encode(encoding="utf-8")
# b = base64.b64encode(bytestring).decode().strip()
# print(b)