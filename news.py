from datetime import date, timedelta
import requests


class NewsFeed:
    def __init__(self, theme='interesting', days_ago=0, language='en', country=None, page_size=10):
        self.theme = theme
        self.sort_by = 'popularity'
        today = date.today() - timedelta(days_ago)
        self.date = today.isoformat()
        self.language = language
        self.country = country
        self.page_size = str(page_size)
        self.apiKey = 'eb80107f22414d52a56c53b2d39b4888'

    def _create_url(self):
        self.url = 'https://newsapi.org/v2/everything?' + \
                   'q=' + self.theme + \
                   '&sortBy=' + self.sort_by + \
                   '&from=' + self.date + \
                   '&language=' + self.language + \
                   '&pageSize=' + self.page_size + \
                   '&apiKey=' + self.apiKey

        if self.country is not None:
            self.url = 'https://newsapi.org/v2/top-headlines?' + \
                       'country=' + self.country + \
                       '&pageSize=' + self.page_size + \
                       '&apiKey=' + self.apiKey
        return self.url

    def _get_url(self):
        return self.url

    def get_news(self):
        url = self._create_url()
        response = requests.get(url)
        content = response.json()

        list_of_news = ''
        for i in range(len(content['articles'])):
            list_of_news += content['articles'][i]['title'] + '\n'
            list_of_news += content['articles'][i]['url'] + '\n' * 2

        return list_of_news
