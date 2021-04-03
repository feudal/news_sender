import yagmail
import pandas as pd
from datetime import datetime
import time

from news import NewsFeed

while True:
    if datetime.now().hour == 9:
        print('Executing!')
    time.sleep(360)
    df = pd.read_excel('people.xlsx')
    df.to_dict()

    list_of_user = []

    for i in range(len(df)):
        user = {}
        user['name'] = df['name'][i]
        user['surname'] = df['surname'][i]
        user['email'] = df['email'][i]
        user['interest'] = df['interest'][i]
        list_of_user.append(user)

    email = yagmail.SMTP(user='emails.sender.dmitri', password='emails.sender.dmitri1987')

    for i in range(len(list_of_user)):
        news = NewsFeed(f"{list_of_user[i]['interest']}")
        content_for_email = news.get_news()
        email.send(to=list_of_user[i]['email'],
                   subject=list_of_user[i]['interest'],
                   contents=f"Hi, {list_of_user[i]['name']}!\n"
                            f"We bring to you the fresh news about {list_of_user[i]['interest']}\n\n"
                            f"{content_for_email}"
                            f"from Dumitru")
