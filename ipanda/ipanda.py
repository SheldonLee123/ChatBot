#!/usr/bin/python
# -*- coding: utf-8 -*-  
""" 
Created on Tue Dec 26 09:24:50 2017
 
@author: Sheldon
"""  
  
import urllib2  
import urllib  
def chatRobot(words):  
#定义一个要提交的数据数组(字典)  
    data = {}  
  
    data['key'] = 'a2bd87304ad4415baaaee4d249ea7eee'  
    data['info'] = words  
    data['userid'] = '155236'  
  
    #定义post的地址  
    url = 'http://www.tuling123.com/openapi/api'  
    post_data = urllib.urlencode(data)  
   
    #提交，发送数据  
    req = urllib2.urlopen(url,post_data)  
   
    #获取提交后返回的信息  
    content = req.read()  
    #content = str(content)    #content  
    content = content.split('"')
    if len(content)==7:                #判断除了text是否返回其他元素
        print 'ipanda:'+content[5]
    else:
        print 'ipanda:'+content[5]+content[9]
          
    #print content

while(1):
    str = raw_input("Sheldon:")
    chatRobot(str)  
