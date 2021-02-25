import pandas as pd

url='https://s.weibo.com/top/summary?sudaref=www.baidu.com'

tb=pd.read_html(url)
print(type(tb))
print(len(tb))
print(tb[0])