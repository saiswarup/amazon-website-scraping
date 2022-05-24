#Url:https://www.amazon.de/s?bbn=3597086031&rh=n%3A3167641%2Cn%3A%213169011%2Cn%3A3597086031%2Cn%3A13528286031%2Cp_36%3A2000-99999999&dc&fst=as%3Aoff&qid=1507905316&rnid=3597086031&ref=sr_nr_n_0
import subprocess
import os, sys, re, time, gzip
import csv
from tempfile import NamedTemporaryFile
import shutil
import logging
import subprocess
from io import StringIO
import sys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from os import path
import json
from openpyxl import Workbook
wb=Workbook()
ws=wb.create_sheet('AmazonData')

mainUrl="https://www.amazon.de/s?bbn=3597086031&rh=n%3A3167641%2Cn%3A%213169011%2Cn%3A3597086031%2Cn%3A13528286031%2Cp_36%3A2000-99999999&dc&fst=as%3Aoff&qid=1507905316&rnid=3597086031&ref=sr_nr_n_0"
driver = webdriver.Chrome("./chromedriver")
driver.get(mainUrl)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
data=soup.findAll('div',{"class":"a-section a-spacing-medium"})
#print(data)

for data_file in data:
    #print(data_file)
    print('_______________________________')
    Amazon_url="https://www.amazon.de"+data_file.find("a",{"class":"a-link-normal a-text-normal"})['href']
    print(Amazon_url)
    Amazon_title=data_file.find("span",{"class":"a-size-base-plus a-color-base a-text-normal"}).getText().encode('ascii', 'ignore').decode('ascii')
    print(Amazon_title)
    try:
        Amazon_Price=data_file.find("span",{"class":"a-offscreen"}).getText().encode('ascii', 'ignore').decode('ascii')
        Amazon_Price=''.join(re.findall("\d+",Amazon_Price))
        print(Amazon_Price)
    except:
        pass
    row = [Amazon_url, Amazon_title, Amazon_Price]
    ws.append(row)
wb.save('Amazon.xlsx')
