# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
from urllib2 import urlopen  
import csv


franchiseList = {'교촌치킨':29691}


Url = 'http://franchise.ftc.go.kr/fir/manage/searchFrameDetail.do?method=getSearchShow&fir_mst_sn='

for key in franchiseList.keys():
    number = franchiseList[key]

    csv_file = open(str(key)+'.csv', "w")
    cw = csv.writer(csv_file, delimiter=',')

    baseUrl = Url + str(number)
    html = urlopen(baseUrl)
    bs = BS(html)  
    
    print bs

    for x in range(1,5):
        
        ls = []
        for i in bs.select('table')[30].select('td')[4*(x-1):4*(x)]:
            
            ls.append(i.text.encode('utf-8'))
        cw.writerow(ls)
           

    for x in range(1,5):
        
        ls = []
        for i in bs.select('table')[32].select('td')[5*(x-1):5*(x)]:
            
            ls.append(i.text.encode('utf-8'))
        cw.writerow(ls)
           

    for x in range(1,19):
        
        ls = []
        for i in bs.select('table')[34].select('td')[3*(x-1):3*(x)]:
            
            ls.append(i.text.strip(',').encode('utf-8'))
        cw.writerow(ls)


    for x in range(1,3):
        
        ls = []
        for i in bs.select('table')[44].select('td')[5*(x-1):5*(x)]:
            
            ls.append(i.text.encode('utf-8'))
        cw.writerow(ls)