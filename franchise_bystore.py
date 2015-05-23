# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
from urllib2 import urlopen  
from urllib import quote, unquote
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


franchiseList_Chicken = ['BBQ', '페리카나', '네네치킨', '교촌치킨', '처갓집양념치킨', '굽네치킨', '또래오래', 'BHC', '호식이두마리', '부어치킨', '맥시칸치킨', '맘스터치', '지코바']
franchiseList_Coffee = ['카페띠아모','파스쿠찌','할리스','탐앤탐스','투썸플레이스','엔제리너스','이디야','카페베네']
franchiseList_Ddokk = ['아딸','죠스떡볶이','올떡','동대문엽기떡볶이','국대떡볶이','버무리떡볶이','요런떡볶이','신전떡볶이','신참떡볶이']

category = {'Chicken':franchiseList_Chicken,'Ddokk':franchiseList_Ddokk,'Coffee':franchiseList_Coffee}

html_List = []                  

for cat in range(len(category)):


    csv_file = open(str(category.keys()[cat])+'.csv', "w")
    cw = csv.writer(csv_file, delimiter=',')


    for fran in category.values()[cat]:
        ae = quote(fran.encode('EUC-KR'))
        Url1 = 'http://franchise.ftc.go.kr/fir/manage/searchFirList2.do?method=getSearchList&currpage=1&indus=&t_nm=&brd=' 
        Url2 = '&stdate=&enddate=&onelimit=10'
        baseUrl = Url1 + ae + Url2
        html = urlopen(baseUrl)
        bs = BS(html)

        Url3 = 'http://franchise.ftc.go.kr'
        number = bs.select('td.lef a')[1].attrs['href']
        final = Url3 + number
        bs2 = urlopen(final)
        bs3 = BS(bs2)

        html_List.append(bs3)

        cw.writerow([fran.decode('utf-8')])
            
        for x in range(1,5):            
            ls = []
            for i in bs3.select('table')[32].select('td')[4*(x-1):4*(x)]:
                
                ls.append(i.text.encode('utf-8'))
            cw.writerow(ls)
               
        for x in range(1,5):
            ls = []
            for i in bs3.select('table')[34].select('td')[5*(x-1):5*(x)]:
                
                ls.append(i.text.encode('utf-8'))
            cw.writerow(ls)
            
        for x in range(1,19):        
            ls = []
            for i in bs3.select('table')[36].select('td')[3*(x-1):3*(x)]:
                
                ls.append(i.text.strip(',').encode('utf-8'))
            cw.writerow(ls)

        for x in range(1,3):            
            ls = []
            for i in bs3.select('table')[46].select('td')[5*(x-1):5*(x)]:
                
                ls.append(i.text.encode('utf-8'))
            cw.writerow(ls)

        cw.writerow(' ')