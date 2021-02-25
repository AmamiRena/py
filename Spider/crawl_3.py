import requests
import re
from lxml import html,etree

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

def get_html_fromfile():
    res=requests.get("#.html",headers=headers)
    data=res.text
    with open('./crawl_3.html','w',encoding='utf-8') as f:
        f.write(data)

def get_pokemons_fromfile():
    try:
        with open('./crawl_3.html','r',encoding='utf-8') as f:
            data=f.read()
            return data
    except Exception as e:
        return None

def analysis(data):
    tree=html.fromstring(data)
    select=tree.cssselect('div#mw-content-text table[class^=colortable] li')
    for ea in select:
#        print(ea.cssselect('span')[0].get('data-pid'))
#        print(ea.cssselect('a')[0].get('title'))
        print(ea.text_content().strip())

def analysis_xpath(data):
    html=etree.HTML(data)
    content=html.xpath("//div[@class='mf-section-1']//li")
    for ea in content:
        pid=ea.xpath('./text()')[1]
        name=ea.xpath('./a/text()')[0]
        print(pid,name)

if __name__ == '__main__':
#    get_html_fromfile()
    data=get_pokemons_fromfile()
#    analysis(data)
    analysis_xpath(data)