# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Assignment 9
# Description:
# get show time from music venus chosen

import os
from bs4 import BeautifulSoup as bs
import urllib.request
import ssl

def store_webpage(url, ctx, fn):
    page = urllib.request.urlopen(url, context=ctx)
    soup = bs(page.read(), 'html.parser')
    f = open(fn, 'w')
    print(soup, file=f)
    f.close()
def load_webpage(url, ctx):
    page = urllib.request.urlopen(url, context=ctx)
    return bs(page.read(), 'html.parser')

def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # the code for storing the webpage locally
    web_url = 'https://www.cryptoarena.com/events'
    file_name = 'sites/crptoarena.html'
    web_url2 = "https://www.lagreektheatre.com/"
    file_name2 = 'sites/lagreektheatre.html'
    # Uncomment below line and run ONCE to save file locally
    # store_webpage(web_url, ctx, file_name)
    # store_webpage(web_url2, ctx, file_name2)
    file_url = 'file:///' + os.path.abspath(file_name)
    file_url2 = 'file:///' + os.path.abspath(file_name2)
    soup = load_webpage(file_url, ctx)
    soup2 = load_webpage(file_url2,ctx)
    soup_month = soup.find_all("span",class_="m-date__month")
    soup_date = soup.find_all("span",class_="m-date__day")
    soup_headerline = soup.find_all("h3", class_="title")
    soup2_month = soup2.find_all("span",class_="m-date__month")
    soup2_date = soup2.find_all("span",class_="m-date__day")
    soup2_headerline = soup2.find_all("h3",class_="m-eventItem__title m-eventItem__title-withTagline")
    print("Concerts Coming up at crptoarena:")
    for i in range(len(soup_month)):
        print("\t" + soup_month[i].text + "" + soup_date[i].text + soup_headerline[i].text)
    print("\nConcerts Coming up at lagreektheatre:")
    for i in range(len(soup2_month)):
        print("\t" + soup2_month[i].text + "" + soup2_date[i].text + soup2_headerline[i].text)



if __name__ == '__main__':
    main()