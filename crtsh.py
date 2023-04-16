import sys
import requests as rq
import re
import os
import pandas as pd

cleanr = re.compile("<.*?>")

def unique(list1):
    unique_list = pd.Series(list1).drop_duplicates().tolist()
    for x in unique_list:
        print(x)


def crtsh():
    url = "https://crt.sh?q=google.com"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0."}
    res = rq.get(url, headers=headers)
    response = res.text
    cleantext = re.sub(cleanr, '\n', response)
    s =re.findall(r"[a-zA-Z]*?/*.google.*", cleantext)
    unique(s)
crtsh()
