import urllib
from bs4 import BeautifulSoup
import requests
import re
import json
import pprint

def peReport():

    USER = "XXXXXXXXXX"
    PASS = "XXXXXXXXXX"

    session = requests.session()

    login_info = {
        "username":USER,
        "password":PASS
    }

    url_login = "https://xxxxxxxxxxxxx"

    res = session.post(url_login, data=login_info)

    res.raise_for_status() # エラーならここで例外を発生させる

    soup = BeautifulSoup(res.text, 'lxml')

    for target in re.findall("var filingData =.*;" , soup.text):
        firstDel = target[19:]
        lastDel = firstDel[:len(firstDel)-3]
        strlist = lastDel.split("},{")
        jsonList = []
        nameList = "未提出者"
        for str in strlist :
            strPlus = "{"+str+"}"
            strReplace = strPlus.replace("\'","\"")
            # print(strReplace)
            jsonList.append(json.loads(strReplace))
        for jsonData in jsonList :
            if jsonData['filingDatetime'] is None :
                nameList =  nameList+"\n"+ jsonData['staffName']
        return nameList