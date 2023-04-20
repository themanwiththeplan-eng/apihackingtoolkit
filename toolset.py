# Call function to take in positional arguments, if those arguments match with a specific letter or keyword then executabe a given other function

import sys
import fileinput
from urllib import response
import requests as rq
import argparse as args
import pandas as pd
from tkinter import *
import re


parser = args.ArgumentParser(description="Insert arguments for API hacking toolsuite")    
parser.add_argument('-d', '--domain')
parser.add_argument('-s', '--subdomain')
parser.add_argument('-dir', '--directories')
parser.add_argument('-v','--verbose', action="store_true")
parser.add_argument('-c', '--curl')
parser.add_argument('-g', '--gui')
parser.add_argument('-done')
arguments = parser.parse_args()

cleanr = re.compile("<.*?>")

def unique(list1):
    unique_list = pd.Series(list1).drop_duplicates().tolist()
    for x in unique_list:
        print(x)


def crtsh():
    url = "https://crt.sh?q=" + arguments.domain
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0."}
    res = rq.get(url, headers=headers)
    response = res.text
    cleantext = re.sub(cleanr, '\n', response)
    s =re.findall(r"[a-zA-Z]*?/*." + arguments.domain + ".*", cleantext)
    unique(s)


def startGui():
    root =Tk()
    root.title("hAPI Toolkit :D")
    root.configure(background="Black")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")
    def enumerate_subdomains():
        global entry
        domain1 = domain.get()
        entryfile1 = entryfile.get()
        file = open(entryfile1, "r")
        lines = file.readlines()
        for l in lines:
           l = l.strip("\n")
           url = "https://" + l + "." + domain1
           get = rq.get(url)
           getRes = get.status_code
           print(url + " " + str(getRes))
    def dir_bruteforce():
        global entry
        domain1 = domain.get()
        entryfile1 = entryfile.get()
        file = open(entryfile1, "r")
        lines = file.readlines()
        for l in lines:
            l = l.strip("\n")
            url = "https://" + domain1 + "/" + l
            get=rq.get(url)
            getRes=get.status_code
            print(url + " " + str(getRes))
    Label(root, text="Domain", bg="black").grid(row=0, column=1, padx=5, pady=5, sticky=E)
    domain = Entry(root, bd=3)
    domain.grid(row=0, column=2, columnspan=4, padx=5, pady=5)
    Label(root, text="File", bg="black").grid(row=1, column=1, padx=5, pady=5, sticky=E)
    entryfile = Entry(root, bd=3)
    entryfile.grid(row=1, column=2, columnspan=4, padx=5, pady=5)
    runDir = Button(root, text="Directory BruteForce", command=dir_bruteforce)
    runDir.grid(row=2, column=2, columnspan=4, padx=5, pady=5)
    runSub = Button(root, text="Subdomain Enumeration", command=enumerate_subdomains)
    runSub.grid(row=3, column=2, columnspan=4, padx=5, pady=5)
    label = Label(root, text="", font=("Courier 22 bold"))
    label.grid(row=20, column=2, columnspan=4, padx=5, pady=5)
    quit = Button(root, text="Quit", command=root.quit)
    quit.grid(row=4, column=2, columnspan=4, padx=5, pady=5)
    root.mainloop()

startGui()



def startProgram():
    if(arguments.curl):
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
            crtsh()



# TODO: Add more functionality to curl
# TODO: Add more to the gui and get it to work when an argument is passed 
# TODO: Get crtsh function to work within the subdomain enumeration module
# TODO: Make file into a button to be able to upload a file and loop line by line, and append to end of domain with function buttons
# TODO: Fix vhost enumeration to not throw an error, when doing more than one subdomain
# startProgram()
