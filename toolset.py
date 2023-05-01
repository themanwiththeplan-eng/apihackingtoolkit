# Call function to take in positional arguments, if those arguments match with a specific letter or keyword then executabe a given other function:w

import sys
import fileinput
from urllib import response
import requests as rq
import argparse as args
import pandas as pd
from tkinter import *
import re
from crtsh import *
from gui import *

parser = args.ArgumentParser(description="Insert arguments for API hacking toolsuite")    
parser.add_argument('-d', '--domain')
parser.add_argument('-s', '--subdomain')
parser.add_argument('-dir', '--directories')
parser.add_argument('-v','--verbose', action="store_true")
parser.add_argument('-c', '--curl')
parser.add_argument('-g', '--gui')
parser.add_argument('--headers')
parser.add_argument('--github')
parser.add_argument('-done')
arguments = parser.parse_args()

cleanr = re.compile("<.*?>")

startGui()

def startProgram():
    if(arguments.curl):
        if(arguments.headers):
            # add headers here
            return
        response = rq.get("https://" + arguments.curl)
        print(response.text)
        status = response.status_code
        if (status >= 200 and status <= 400):
            print (status)
        elif(status >= 400):
            print(f"{status}", "is not okay")
    elif (arguments.domain):
        if(arguments.directories):
            file = open(arguments.directories, "r")
            lines = file.readlines()
            for l in lines:
                l = l.strip("\n")
                url = "https://" + arguments.domain + "/" + l
                get = rq.get(url)
                post = rq.post(url)
                getResponse = get.status_code
                postResponse = post.status_code
                print("GET:",f"{url}", f"{getResponse}")
                print("POST:", f"{url}", f"{postResponse}")
        elif(arguments.subdomain):
            file = open(arguments.subdomain, "r")
            lines = file.readlines()
            for l in lines:
                l = l.strip("\n")
                url = "https://" + l + "." + arguments.domain
                get = rq.get(url)
                post = rq.post(url)
                getRes = get.status_code
                postRes = post.status_code
                print ("GET:", f"{url}", f"{getRes}")
                print("POST:", f"{url}", f"{postRes}")
            crtsh(arguments.domain)
        elif(arguments.github):
            #TODO: introduce scraping for secrets on github using regex patterns
            return


# TODO: Add more functionality to curl
# TODO: Add more to the gui and get it to work when an argument is passed 
# TODO: Get crtsh function to work within the subdomain enumeration module
# TODO: Make file into a button to be able to upload a file and loop line by line, and append to end of domain with function buttons
# TODO: Fix vhost enumeration to not throw an error, when doing more than one subdomain
# startProgram()

