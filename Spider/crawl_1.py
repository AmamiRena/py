import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}
i=1
course_list=[]
while i>0:
    url="#{i}".format(i=i)
    res=requests.get(url=url,headers=headers)
    html_data=res.text
    course=re.findall('<h6 title="(.*)" class="course-name"',html_data)
    course_list+=course
    i+=1
    if len(course)==0:
        break

for ea in course_list:
    new_str="课程：{ea}\n".format(ea=ea)
    with open('./course_list.txt','a',encoding="utf-8") as f:
        f.write(new_str)