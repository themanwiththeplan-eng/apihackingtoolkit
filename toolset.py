# Call function to take in positional arguments, if those arguments match with a specific letter or keyword then executabe a given other function

import sys
import fileinput
from urllib import response
import requests as rq
import argparse as args
import pandas as pd


parser = args.ArgumentParser(description="Insert arguments for API hacking toolsuite")    
parser.add_argument('-w', '--wordlist')
parser.add_argument('-d', '--domain')
parser.add_argument('-s', '--subdomain')
parser.add_argument('-dir', '--directories')
parser.add_argument('-v','--verbose', action="store_true")
parser.add_argument('-done')
arguments = parser.parse_args()

def startProgram():
    if(arguments.domain):
        response = rq.get(arguments.domain)
        print(response)
    elif (arguments.domain, arguments.wordlist):
        file = open(arguments.wordlist, "r")
        lines = file.readlines()
        for l in lines:
            get = rq.get(arguments.domain + "/" + l)
            post = rq.post(arguments.domain + "/" + l)
            getResponse = get.json
            postResponse = post.json
            print("GET:"f"{getResponse}")
            print("POST:",f"{postResponse}")
    
        





startProgram()