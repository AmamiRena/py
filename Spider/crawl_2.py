import requests
import re
import time

#source='<li><a href="/details?id=com.ss.android.ugc.aweme"><img data-src="http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/024175a95820a116bd5cec07df87433286440d087" src="http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/024175a95820a116bd5cec07df87433286440d087" alt="抖音" width="72" height="72"></a><h5><a href="/details?id=com.ss.android.ugc.aweme">抖音</a></h5><p class="app-desc"><a href="/category/27">影音视听</a></p></li>'

headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"}

def save_img(url,name,note):
    img_res=requests.get(url=url,headers=headers)
    if img_res.status_code==requests.codes.ok:
        data=img_res.content
        with open('./icons/{name}({note}).png'.format(name=name,note=note),'wb') as f:
            f.write(data)
        print('{name}({note})-saved'.format(name=name,note=note))

def get_item(page=1):
    url='#{page}'.format(page=page)
    res=requests.get(url=url,headers=headers)
    if res.status_code==requests.codes.ok:
        html=res.text
        pattern=re.compile(r'<li><a href=".*?"><img data-src="(.*?)" src=".*?" alt=".*?" width=".*?" height=".*?"></a><h5><a href=".*?">(.*?)</a></h5><p class=".*?"><a href=".*?">(.*?)</a></p></li>')
        items=pattern.findall(html)
        print(items)
        for item in items:
            save_img(item[0],item[1],item[2])

if __name__=="__main__":
    for page in range(1,3):    #only 2 pages
        print('Spdering Page {page}'.format(page=page))
    get_item()
    time.sleep(2)
