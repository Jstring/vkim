
#-*- coding: utf-8 -*-


import csv
import requests
import datetime
from bs4 import BeautifulSoup as bs
from time import sleep
import argparse


class ilbe(object):
    def __init__(self,query,menu="celeb"):
        self.user_agent={'User-agent': 'Mozilla/5.0'}
        self.query=query
        self.menu=menu

    def url_scraper(self):
        url_list=list()
        user_agent =self.user_agent
        query=str(self.query)
        menu=str(self.menu)
        url="http://www.ilbe.com/?_filter=search&mid="+menu+"&category=&search_target=title&search_keyword="+query
        #table=music부분이 변하는부분
        

        page=1
        while True:
            page_url=url+"&page="+str(page)
            print(page_url)
            page_source=requests.get(page_url,headers=user_agent).text
            tmp=bs(page_source)
            tmp_list=tmp.select('tr[class^=bg]')

            if not tmp_list:
                break
                
            for i in range(22):
                try:
                    content_url=str(tmp.select('tr[class^=bg]')[i].select('a')[0])
                    content_url=content_url.split('"')[1].replace('amp;','')
                    text_number=content_url.split('=')[-1]
                    text_subject=tmp.select('tr[class^=bg]')[i].select('td[class=title]')[0].text.strip()
                    text_subject=replace_all(text_subject)

                    text_writer=tmp.select('tr[class^=bg]')[i].select('td[class=author]')[0].text.strip()
                    text_time=tmp.select('tr[class^=bg]')[i].select('td[class=date]')[0].text.strip()
                    text_time=replace_all(text_time)

                    lst=content_url,text_number,text_subject,text_writer,text_time
                    url_list.append(lst)
                except:
                    pass
    
            page=page+1
        
        return (url_list)
    
ilbe("힙합","celeb").url_scraper()