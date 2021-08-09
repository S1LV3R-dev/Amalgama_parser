import requests
from lxml import etree
import lxml.html
import csv
import re

songname = ""

def parse(url):
    try:
        api = requests.get(url)
    except:
        global songname
        with open("errors.txt", 'w') as f:
            f.write("Couldn't get "+songname)
        return
    tree = lxml.html.document_fromstring(api. text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    with open(songname+".txt","w") as f:
        for i in range(len(text_original)):
            if(text_original[i][0] != '[' and
               text_translate[i][0] != '[' and
               text_original[i][-1] != ']' and 
               text_translate[i][-1] != ']'):
                f.write(text_original[i])
                f.write(text_translate[i])
                f.write('\n')

def htmltoname(url):
    global songname
    songname = url.split('/')[-1][:-5]

def main():
    url = input("Enter song link")
    htmltoname(url)
    parse(url)


if __name__ == "__main__":
    main()
