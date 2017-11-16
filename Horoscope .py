"""
Project : Horoscope finder
Author : Ajeet
Date : 12/11/2017
"""

import urllib2
from bs4 import BeautifulSoup
import time


def horoscope1(sign):
    print "Fetching data.......\n"
    global a
    response = urllib2.urlopen("http://www.tarot.com/daily-horoscope/"+sign).read()
    soup = BeautifulSoup(response,"lxml")

    for p in soup.find_all('p',class_="js-today_interp_copy"):
        a= p.text
        
        print a

############################################    
def horoscope2(sign):
    print "\nFetching data......."
    global c
    response = urllib2.urlopen("https://new.theastrologer.com/"+sign+"/").read()
    soup = BeautifulSoup(response,"lxml")


    for div in soup.find_all('div',class_="tab-pane active"):
        p=div.find_all('p')
        for p1 in p:
            c= p1.text
            
            print "\n",c
            break

###########################################
def horoscope3(sign):
    print "\nFetching data......."
    global d
    response = urllib2.urlopen("https://www.astrology.com/horoscope/daily/"+sign+".html").read()
    soup = BeautifulSoup(response,"lxml")


    for div in soup.find_all('div',class_="daily-horoscope"):
        d=div.find('p').text
        
        print "\n",d
        


###########################################
def print1():
        horoscope1(moon_sign)
        horoscope2(moon_sign)
        horoscope3(moon_sign)

while True:
    try:
        moon_sign=raw_input("Your moon sign : ").lower()
        
        print1()

        #Posting on fb 
        import fbconsole as fb
        fb.AUTH_SCOPE = ['public_profile', 'user_friends','manage_pages']
        fb.APP_ID = '738141636393999'
        fb.authenticate()
        fb.post('/me/feed/', {'message':'Today\'s Horoscope : '+moon_sign+'\n\n'+a})
        fb.post('/me/feed/', {'message':'Today\'s Horoscope : '+moon_sign+'\n\n'+c})
        fb.post('/me/feed/', {'message':'Today\'s Horoscope : '+moon_sign+'\n\n'+d})
        fb.logout()
        break

        
    except urllib2.HTTPError:
        
        print "Entered sign is incorrect.Please enter coorect one"
        time.sleep(1)
   



