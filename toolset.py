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
parser.add_argument('-g', '--gui')
parser.add_argument('-done')
arguments = parser.parse_args()



def startGui():
    root =Tk()
    root.title("hAPI Toolkit :D")
    root.configure(background="Black")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")
    Label(root, text="Domain", bg="black").grid(row=0, column=1, padx=5, pady=5, sticky=E)
    domain = Entry(root, bd=3)
    domain.grid(row=0, column=2, columnspan=4, padx=5, pady=5)
    runDir = Button(root, text="Directory BruteForce")
    runDir.grid(row=2, column=2, columnspan=4, padx=5, pady=5)
    runSub = Button(root, text="Subdomain Enumeration")
    runSub.grid(row=3, column=2, columnspan=4, padx=5, pady=5)
    quit = Button(root, text="Quit", command=root.quit)
    quit.grid(row=4, column=2, columnspan=4, padx=5, pady=5)
    root.mainloop()

# startGui()



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
        



# TODO: Add more functionality to curl
# TODO: Add more to the gui and get it to work when an argument is passed 


startProgram()


