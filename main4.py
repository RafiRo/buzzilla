from pprint import pprint
from bs4 import BeautifulSoup
import sys
from urllib import request
import re



def main():
    urls = ["http://ynet.co.il","http://he.wikipedia.org","http://www.talniri.co.il"]
    func(urls)

def func(urls):
    soup = ''
    # CONCATANATE ALL LINKS SOURCE CODE
    for url in urls:
        contents = request.Request(url)
        response = request.urlopen(contents)
        tempsoup = BeautifulSoup(response,"html.parser").get_text()
        soup = soup + tempsoup + '\n'


    #Find all Hebrew words with regex
    result = re.findall("[\u0590-\u05FE]*", soup)
    filterList = list(filter(None, result)) #Clear empty groups

    #Convert to Hash
    words={}
    for i in filterList:
        if len(i) not in words.keys():
            words[len(i)] = {}

        if i in words[len(i)].keys():
            words[len(i)][i] = words[len(i)][i] + 1
        else:
            words[len(i)][i] = 1


    keys = list(words.keys())
    keys.sort()

    #Prints the most common words
    for i in keys:
        tempHash = {}
        for ii in words[i]:
            tempHash[words[i][ii]] = ii
        maxNumber = max(tempHash.keys())
        print("LEN "+ str(i) +' : ' +tempHash[maxNumber])



main()