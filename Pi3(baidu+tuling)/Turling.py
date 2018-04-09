# coding: utf-8

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def Turing(words):
    Tuling_API_KEY = "a2bd87304ad4415baaaee4d249ea7eee"

    body = {"key":Tuling_API_KEY,"info":words.encode("utf-8"),"userid":'155236'}

    url = "http://www.tuling123.com/openapi/api"
    r = requests.post(url,data=body,verify=True)

    if r:
        data = json.loads(r.text)
        if len(data) == 2:
            print 'ipanda:'+data["text"]
            return data["text"]
        else:
            print 'ipanda:'+data["text"]+data["url"]
            return data["text"]+data["url"]
    else:
        return None

#while True:
    #str = raw_input("Sheldon:")
    #Turling(str)  
