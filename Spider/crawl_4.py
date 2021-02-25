import requests
from bs4 import BeautifulSoup

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

def get_detail():
    r=requests.get('#',headers=headers)
    html=r.text
    soup=BeautifulSoup(html,'lxml')
    div_tags=soup.select("div[class='y-book-item']")
    book_list=[]
    for div in div_tags:
        link=div.a.attrs['href']
        img=div.find('img').attrs['src']
        name=div.select('h3')[0].get_text()
        book_list.append((link,img,name))
#        print(link,img,name)
    return book_list

def write_in(book_list):
    for ea in book_list:
        new_str='{ea}\n'.format(ea=ea)
        with open('./book_list.txt','a',encoding='utf-8') as f:
            f.write(new_str)

if __name__=='__main__':
    book_list=get_detail()
    write_in(book_list)