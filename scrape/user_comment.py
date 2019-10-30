import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "https://www.forexfactory.com/showthread.php?t=948113"
r = requests.get(URL)  
soup = BeautifulSoup(r.content, 'html5lib') 
# table = soup.find('div', attrs = {'class':'showthread showthread--anchored flexBox noflex'}) 
table = soup.findAll('div', attrs = {'class':'showthread showthread--anchored flexBox noflex'}) 

# for item in table:
#     name = item.find(class_='usernamedisplay__username username').get_text()
#     comment = item.find(class_='threadpost-content__message').get_text()


with open("E:/shpro/Output.txt", "w", encoding='utf-8') as text_file:
    for item in table:
        # print(item)
        name = item.find(class_='usernamedisplay__username username').get_text()
        comment = item.find(class_='threadpost-content__message').get_text()
        text_file.write('User_Name: '+name)
        text_file.write('\n')
        # print(name)
        # print(comment)
        text_file.write('Comments: '+comment)
        text_file.write('############################################################')
        text_file.write('\n')

 
for i in range(2,50):
    print(i)
    URL = "https://www.forexfactory.com/showthread.php?t=948113&page="+str(i)
    r = requests.get(URL)  
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('div', attrs = {'class':'showthread showthread--anchored flexBox noflex'})     
    with open("E:/shpro/Output.txt", "a+", encoding='utf-8') as text_file:
        for item in table:
            # print(item)
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

                # print(name)
                # print(comment)
                text_file.write('############################################################')
                text_file.write('\n')
