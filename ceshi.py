# -*- coding: utf-8 -*-
import http.client, urllib
import json      #引入json库
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'58a01e0a0e30464e48d0f0633ca57867'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/lzmy/index',params,headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)  #转换成字典
data=data.get("newslist", "未找到值")[0]
data=data.get("saying","未找到值")
print (data)
