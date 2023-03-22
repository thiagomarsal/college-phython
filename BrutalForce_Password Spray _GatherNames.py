#!/usr/bin/python3

import requests
import re

# Use the below to supress the warnings due to not verifying the SSL/TLS certs
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def saveWebPage(urls, fileName):
    for url in urls:
        r = requests.get(url,verify=False)
        with open(fileName,'a') as f:
            #print(r.content)
            f.write(r.text)

def extractNames(fileName):
    nameList = []
    with open(fileName, 'r') as f:
        for line in f:
            firstLastName = re.findall(r"[A-Z][a-z]+\s[A-Z][a-z]+", line)
            firstMLastName = re.findall(r"[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+", line)
            if len(firstLastName) > 0:
                for i in firstLastName:
                    if i not in nameList:
                        nameList.append(i)
            if len(firstMLastName) > 0:
                for i in firstMLastName:
                    if i not in nameList:
                        nameList.append(i)
    for name in nameList:
        print(name)

def main():
    urls = ["https://www.website.web", "https://www.website.web/about"]
    fileName = "output.html"
    saveWebPage(urls, fileName)
    extractNames(fileName)