import os
import urllib
# import urllib2
import requests 
from bs4 import BeautifulSoup 
from random import randint
import csv 
  
URL = "https://www.forexfactory.com/showthread.php?t=948113"

r = requests.get(URL)  
soup = BeautifulSoup(r.content, 'html5lib') 
# table = soup.find('div', attrs = {'class':'showthread showthread--anchored flexBox noflex'}) 
table = soup.findAll('div', attrs = {'class':'showthread showthread--anchored flexBox noflex'}) 

userName = {}
# imgs = table.findAll("img", {"class":"attach"})
# new = "why"
# os.mkdir('E:/shpro/'+new)
# basepath ='E:/shpro/'+new
# for im in imgs:
#     img = im['src']
#     imgUrl = 'https://www.forexfactory.com/'+img
#     name =  str(randint(0, 10000))+".png"
#     urllib.request.urlretrieve(imgUrl,os.path.join(basepath, name))
# print(basepath)



# for item in table:
#     name = item.find(class_='usernamedisplay__username username').get_text()
#     comment = item.find(class_='threadpost-content__message').get_text()


with open("E:/shpro/Scrape/Output.txt", "w", encoding='utf-8') as text_file:
    for item in table:
        name = item.find(class_='usernamedisplay__username username').get_text()
        comment = item.find(class_='threadpost-content__message').get_text()
        text_file.write('User_Name: '+name)
        text_file.write('\n')
        text_file.write('Comments: '+comment)
        text_file.write('############################################################')
        text_file.write('\n')
        imgs = item.findAll("img", {"class":"attach"})
        if imgs is not None and len(imgs)>0:
            new = name
            if name not in userName:
                os.mkdir('E:/shpro/Scrape/'+new)
                userName[name] = name
            basepath ='E:/shpro/Scrape/'+new
            for im in imgs:
                img = im['src']
                imgUrl = 'https://www.forexfactory.com/'+img
                name =  str(randint(0, 10000))+".png"
                urllib.request.urlretrieve(imgUrl,os.path.join(basepath, name))


 
for i in range(2,50):
    print(i)
    URL = "https://www.forexfactory.com/showthread.php?t=948113&page="+str(i)
    r = requests.get(URL)  
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('div', attrs = {'class':'showthread showthread--anchored flexBox noflex'})     
    with open("E:/shpro/Scrape/Output.txt", "a+", encoding='utf-8') as text_file:
        for item in table:
            if item is not None:
                name = item.find(class_='usernamedisplay__username username')
                if name is not None:
                    name = item.find(class_='usernamedisplay__username username').get_text()
                    text_file.write('User_Name: '+name)
                    text_file.write('\n')
                comment = item.find(class_='threadpost-content__message')
                if comment is not None:
                    comment = item.find(class_='threadpost-content__message').get_text()
                    text_file.write('Comments: '+comment)
                    text_file.write('\n')
                text_file.write('############################################################')
                text_file.write('\n')
                imgs = item.findAll("img", {"class":"attach"})
                if imgs is not None and len(imgs)>0 and name is not None:
                    new = name
                    if name not in userName:
                        os.mkdir('E:/shpro/Scrape/'+new)
                        userName[name] = name
                    basepath ='E:/shpro/Scrape/'+new
                    for im in imgs:
                        img = im['src']
                        imgUrl = 'https://www.forexfactory.com/'+img
                        name =  str(randint(0, 10000000))+".png"
                        urllib.request.urlretrieve(imgUrl,os.path.join(basepath, name))
