from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='feef93a82f4c4635bb86241124c102f6')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='Virat Kohli',
                                          category='business',
                                          language='en')


dt = top_headlines['articles']

for x,y in enumerate(dt):
    print(f'{x}{y["description"]}')