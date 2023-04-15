import sys
import requests as rq
import re
import os

cleanr = re.compile("<.*?>")


def crtsh():
    url = "https://crt.sh?q=google.com"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0."}
    res = rq.get(url, headers=headers)
    response = res.text
    cleantext = re.sub(cleanr, '\n', response)
    s =re.findall(r"[a-zA-Z]*?/*.google.*", cleantext)
    for i in s:
        print(i)

        # TODO: sort this value uniquely then add to toolset.py for more subdomain enumeration
crtsh()