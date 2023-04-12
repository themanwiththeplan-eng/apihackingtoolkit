# Call function to take in positional arguments, if those arguments match with a specific letter or keyword then executabe a given other function

import sys
import fileinput
from urllib import response
import requests as rq
import argparse as args
import pandas as pd
from tkinter import *


parser = args.ArgumentParser(description="Insert arguments for API hacking toolsuite")    
parser.add_argument('-d', '--domain')
parser.add_argument('-s', '--subdomain')
parser.add_argument('-dir', '--directories')
parser.add_argument('-v','--verbose', action="store_true")
parser.add_argument('-c', '--curl')
parser.add_argument('-done')
arguments = parser.parse_args()

def startProgram():
    if(arguments.curl):
        response = rq.get(arguments.curl)
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
                get = rq.get(arguments.domain + "/" + l)
                post = rq.post(arguments.domain + "/" + l)
                getResponse = get.json
                postResponse = post.json
                print("GET:", f"{getResponse}")
                print("POST:",f"{postResponse}")
        elif(arguments.subdomain):
            file = open(arguments.subdomain, "r")
            lines = file.readlines()
            for l in lines:
                l = l.strip("\n")
                url = "https://" + l + "." + arguments.domain
                get = rq.get(url)
                post = rq.post(url)
                getResponse = get.status_code
                postRes = post.status_code
                print ("GET:", f"{getResponse}")
                print("POST:", f"{postRes}")

        





startProgram()

def startGui():
    root =Tk()
    root.title("hAPI Toolkit :D")
    root.configure(background="Black")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")
    root.mainloop()