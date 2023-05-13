import requests as rq
import re
import pandas as pd

cleanr = re.compile("<.*?>")

def unique(list1):
    unique_list = pd.Series(list1).drop_duplicates().tolist()
    for x in unique_list:
        print(x)

def shodan(domain):
    url = "https://www.shodan.io/search?query=" + domain
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0."}
    res = rq.get(url, headers=headers)
    response = res.text
    cleantext = re.sub(cleanr, '\n', response)
    s =re.findall(r"[a-zA-Z]*?/*." + domain + ".*", cleantext)
    unique(s)