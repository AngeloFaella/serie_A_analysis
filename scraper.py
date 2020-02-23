from bs4 import BeautifulSoup
import requests


def scrape_table(url):
        
    # request HTML page
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {"user-agent": user_agent}
    req = requests.get(url, headers=headers)

    # get table
    soup = BeautifulSoup(req.text, "html.parser")
    table = soup.find("div", {"id": "classifiche"})
    table = table.find("table", {"class": "classifica tabella"})
    table = table.find("tbody")
    
    #print(table)
    if table == None:
        return
    
    # extract info from table
    data = ''
    dataset = open('serie_A_'+ url[-7:] +'.csv', 'a')
    rows = table.findAll('tr')
    for row in rows:
        cols = row.findAll('td')
        head = cols[0]
        data += head.find('span').text + ',' # pos
        data += str(head.text)[3:].strip() # name 
        cols = cols[1:]

        for col in cols: # add other stats
            data += ',' + col.text

        data += '\n'
        #print(data)

    # write to .csv    
    dataset.write(data)
    dataset.close()
    print('Done')
   


### MAIN
links = ['http://www.legaseriea.it/it/serie-a/classifica/2018-19',
        'http://www.legaseriea.it/it/serie-a/classifica/2017-18',
        'http://www.legaseriea.it/it/serie-a/classifica/2016-17',
        'http://www.legaseriea.it/it/serie-a/classifica/2015-16',
        'http://www.legaseriea.it/it/serie-a/classifica/2014-15',
        'http://www.legaseriea.it/it/serie-a/classifica/2013-14',
        'http://www.legaseriea.it/it/serie-a/classifica/2012-13',
        'http://www.legaseriea.it/it/serie-a/classifica/2011-12',
        'http://www.legaseriea.it/it/serie-a/classifica/2010-11',
        'http://www.legaseriea.it/it/serie-a/classifica/2009-10',
        'http://www.legaseriea.it/it/serie-a/classifica/2008-09',
        'http://www.legaseriea.it/it/serie-a/classifica/2007-08',
        'http://www.legaseriea.it/it/serie-a/classifica/2006-07',
        'http://www.legaseriea.it/it/serie-a/classifica/2005-06',
        'http://www.legaseriea.it/it/serie-a/classifica/2004-05',
        'http://www.legaseriea.it/it/serie-a/classifica/2003-04',
        'http://www.legaseriea.it/it/serie-a/classifica/2002-03',
        'http://www.legaseriea.it/it/serie-a/classifica/2001-02',
        'http://www.legaseriea.it/it/serie-a/classifica/2000-01',
        'http://www.legaseriea.it/it/serie-a/classifica/1999-00']


for link in links:
    print('Scraping '+link)
    scrape_table(link)

## pos, name, PT, G, V, N, P, ... , F, S