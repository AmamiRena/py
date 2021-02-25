import requests
from bs4 import BeautifulSoup

headers={
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

def get_html():
    res=requests.get('https://s.weibo.com/top/summary',headers=headers)
    return res.text

def analysis_html():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    data=soup.find(name='tbody')
    items=data.find_all(name='tr')
    send_msgs=[]
    for ea in items:
        order_number=ea.find(attrs={'class':'td-01'}).text
        if order_number=='':
            order_number=0
        title_content=ea.find(attrs={'class':'td-02'}).text
        title=''
        readers=''
        if len(title_content)>3:
            print(title_content)
            title=title_content[1].text
            readers=title_content[3].text
        else:
            title=title_content[1].text
            readers='0'
        level=ea.find(attrs={'class':'td-03'}).text
#        print(order_number,title,readers,level)
        send_msgs.append((order_number,title,readers,level))
    return send_msgs

if __name__=='__main__':
    analysis_html()