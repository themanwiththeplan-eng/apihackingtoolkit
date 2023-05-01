import sys
import fileinput
from urllib import response
import requests as rq
import argparse as args
import pandas as pd
from tkinter import *
import re

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


