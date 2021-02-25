import requests
import time

headers={
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

timeout=''

def get_items(timeout):
    url="#"

    data={'type':'tag',
         'channel':"faxian",
         'search_key':'白菜党',
         'timesort':timeout}
    
    res=requests.get(url=url,params=data,headers=headers)
    json_data=res.json()
    goods=json_data['data']
    if len(goods)>0:
        print(len(goods),'in total')
        print(goods)

        last_data=goods[-1]
        timeout=last_data['time_sort']
        print(timeout)
        time.sleep(2)
        get_items(timeout)

if __name__=='__main__':
    get_items(timeout)