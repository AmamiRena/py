import requests
import re

headers = {
    "origin":"#",
    "referer":"#/6512/",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

cookies={'session':'cookies...'}

def thumbup(qid):
    url="#/{qid}/like/".format(qid=qid)
    r=requests.put(url,headers=headers,cookies=cookies)
    content=r.text
    print(content)

def signin():
    url="#/checkin/"
    r=requests.post(url,headers=headers,cookies=cookies)
    content=r.text
    print(content)

if __name__=='__main__':
    thumbup('6512')
    signin()