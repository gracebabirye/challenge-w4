import requests
import click
import urllib.request

news_source_list = []


def get_source_list():
       try:
              sources_url = ('https://newsapi.org/v2/top-headlines?'
              'country=us&'
              'apiKey=6ad19820c0aa4d8fb7a2120159cf6bf8')

              response = requests.get(sources_url)
              items = response.json()

              articles = items['articles']
              for i in articles[0:4]:
                     dictn = {}
                     dictn = {'id': i['source']['id'], 'name': i['source']['name']}
                     news_source_list.append(dictn)
              return news_source_list
       except urllib.error.HTTPError as e:
              raise ConnectionError(e, request=response)
    


def get_source_headlines(sourceid):
       try:
              specific_source_headlines = []

              headlines_url = ('https://newsapi.org/v2/top-headlines?'
                                   'sources=' + sourceid + '&'
                                   'apiKey=6ad19820c0aa4d8fb7a2120159cf6bf8')

              response2 = requests.get(headlines_url)
              headlines = response2.json()
              headline = headlines['articles']
              for i in headline[0:10]:
                     headline_details = {}
                     headline_details = {
                     'title': i['title'], 'description': i['description'], 'url': i['url']}
                     specific_source_headlines.append(headline_details)
              return specific_source_headlines
       except urllib.error.HTTPError as e:
              raise ConnectionError(e, request=response2)


# FETCH NEWS SOURCES
newssources = get_source_list()
if(newssources is list):
       for indx, x in enumerate(newssources):
              print(str(indx + 1) + '. ' + x['name'])

       user_input = input('Enter Number\n')
       sourceid1_id = newssources[int(user_input) - 1]['id']
       if(sourceid1_id != None):
              # #FETCH CHOSEN SOURCE HEADLINES
              newsheadlines = get_source_headlines(sourceid1_id)
              for indx2, x2 in enumerate(newsheadlines):
                     print(str(indx2 + 1) + '. ' + str(x2))
                     print('\n')
       else:
              print("News Source ID is NULL")
else: 
       print("Connection Failure")