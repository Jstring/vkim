# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
from urllib2 import urlopen  
from urllib import quote, unquote
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# franchiseList_Chicken = ['BBQ', '페리카나', '네네치킨', '교촌치킨', '처갓집양념치킨', '굽네치킨', '또래오래', 'BHC', '호식이두마리', '부어치킨', '맥시칸치킨', '맘스터치', '지코바']
# franchiseList_Coffee = ['카페띠아모','파스쿠찌','할리스','탐앤탐스','투썸플레이스','엔제리너스','이디야','카페베네']
# franchiseList_Ddokk = ['아딸','죠스떡볶이','올떡','동대문엽기떡볶이','국대떡볶이','버무리떡볶이','요런떡볶이','신전떡볶이','신참떡볶이']
franchiseList_thebon = ['새마을식당','홍콩반점0410','한신포차','본가','백종원의원조쌈밥','미정국수0410','역전우동0410','홍마반점0410','백스비빔밥','대한국밥','해물떡찜0410','카레왕플러스','최강집','빽다방','성성식당','절구미집','마카오반점0410','한국본갈비','행복분식','알파구이','씨베리안치킨']

category = {'thebon' : franchiseList_thebon}

                  

for cat in range(len(category)):

    html_List = []
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
        bs3  = BS(bs2)

        html_List.append(bs3)

        
    
    cw.writerow(['매장수','년도','가맹점','직영점','계','년도','가맹점','직영점','계','년도','가맹점','직영점','계'])
    for List in category.values()[cat]:
        ls=[List.encode('utf-8'),]
        for i in html_List[category.values()[cat].index(List)].select('table')[32].select('td')[4 :16]:
            ls.append(i.text.encode('utf-8'))
        cw.writerow(ls)
    cw.writerow(['가맹점 변동사항','년도','신규','계약종료','계약해지','명의이전','년도','신규','계약종료','계약해지','명의이전','년도','신규','계약종료','계약해지','명의이전'])
    for List in category.values()[cat]:
        ls=[List.encode('utf-8'),]
        for i in html_List[category.values()[cat].index(List)].select('table')[34].select('td')[5 :25]:
            ls.append(i.text.encode('utf-8'))
        cw.writerow(ls)
    cw.writerow(['지역별','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액','지역','가맹점수','평균매출액'])
    for List in category.values()[cat]:
        ls=[List.encode('utf-8'),]
        for i in html_List[category.values()[cat].index(List)].select('table')[36].select('td')[3 :57]:
            ls.append(i.text.encode('utf-8'))
        cw.writerow(ls)
    cw.writerow(['부담금','가입비(가맹비)','교육비','보증금','기타비용','계']) 
    for List in category.values()[cat]:
        ls=[List.encode('utf-8'),]
        for i in html_List[category.values()[cat].index(List)].select('table')[46].select('td')[5 :15]:
            ls.append(i.text.encode('utf-8'))
        cw.writerow(ls)
