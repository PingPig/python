import re
import urllib.request
import base64
import string
import sys
import linecache
import shodan
import json 
import os
import requests
target = 'app="phpMyAdmin" && country="CN"'
f = open('user_pwd.txt')
d = f.read()
def Fofa_Search_Api(Fofa_target):
    Fofa_email = re.findall(r'fofa_name:"([^"]+)"',d)
    Fofa_key = re.findall(r'fofa_api:"([^"]+)"',d)
    ByteString = Fofa_target.encode(encoding="utf-8")
    Target_Temp = base64.b64encode(ByteString).decode().strip()
    ApiSearchUrl = 'https://fofa.so/api/v1/search/all?email='+Fofa_email[0]+'&key='+Fofa_key[0]+'&qbase64='+Target_Temp+''
    ApiOpen = urllib.request.urlopen(ApiSearchUrl)
    ReString = ApiOpen.read().decode().strip()
    Re_Temp_Dict = re.sub(r'[}{]',' ',ReString)
    Re_Temp_Format = Re_Temp_Dict.split('"results":')[1]
    For_Ip_List = eval(Re_Temp_Format)
    for i in range(len(For_Ip_List)):
        for j in range(0,1):
            print(For_Ip_List[i][j])
def Shodan_Search_Api(Shodan_target):
    Shodan_Api = re.findall(r'shodan_api:"([^"]+)"',d)
    S_Api = Shodan_Api[0]
    S_Api_Check = shodan.Shodan(S_Api)
    Restring = S_Api_Check.search(Shodan_target)
    for Results in Restring['matches']:
        Shodan_Ip_List = Results['ip_str']+":"+str(Results['port'])
        print(Shodan_Ip_List)
def ZoomEyes_Search_Api(Zoomeyes_target):
    Z_Username = re.findall(r'zoomeyes_username:"([^"]+)"',d)
    Z_Password = re.findall(r'zoomeyes_password:"([^"]+)"',d)
    ZU = Z_Username[0]
    ZP = Z_Password[0]
    Page = 1
    Data = {
        'username':ZU,
        'password':ZP
    }
    JsonData = json.dumps(Data,indent=4)
    Login_Url = requests.post('https://api.zoomeye.org/user/login',data=JsonData)
    Login_Restring = json.loads(Login_Url.text)
    AccessToken = Login_Restring['access_token']
    Header = {'Authorization': 'JWT ' + AccessToken,}
    Search_Url = requests.get(url='https://api.zoomeye.org/host/search?query=app:'+Zoomeyes_target+'&page='+ str(Page),headers=Header)
    Rdecode = json.loads(Search_Url.text)
    for i in Rdecode['matches']:
        print(i['ip']+":"+str(i['portinfo']['port']))
if __name__ == "__main__":
    Fofa_Search_Api(target)
    # Shodan_Search_Api(target)
    # ZoomEyes_Search_Api(target)
