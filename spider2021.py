from bs4 import BeautifulSoup
import requests
import csv

f = open("/Users/kasperxiaomingshen/Documents/Dataset/michelin_my_maps2021.csv")
reader = csv.reader(f)
head = next(reader)

for line in reader:
    url = line[10]
    print(url)
    resp = requests.get(url=url)
    raw_html = resp.text
    soup = BeautifulSoup(raw_html, 'lxml')
    info = soup.select('/html/body/main/div/div/div/div/section/div/div/div/p/text()')
    print(info)

f.close()

