#testing some git yeah !!!

import requests
import smtplib
import csv

from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Apple-iPhone-Silver-64GB-Storage/dp/B0711T2L8K/ref=sr_1_1_sspa?keywords=iphone+x&qid=1562856325&s=electronics&sr=1-1-spons&psc=1'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(url, headers=headers )

soup = BeautifulSoup(page.content ,'html5lib' )
#BeautifulSoup(raw, )

title = soup.find(id="productTitle").get_text()
price =soup.find(id="priceblock_ourprice").get_text()

convprice = int(price[2:4])

print(title.strip())
print(convprice)

csvdata = [['product' , 'cost'], ['hello' , 'shahbaaz' ]]

with open('price.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvdata)

csvfile.close()