#-*- coding: utf-8 -*-
import lxml.html
import pandas as pd
import requests
from scraping import bdd

def get_game(bdd, data_id):
    """
    Function to return game product sold on rakuten
    """
    data = [data for data in bdd if data['id'] == data_id]
    page = requests.get(data[0]['url']) 
    html = lxml.html.fromstring(page.content)
    titles = html.xpath("//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span")
    url = html.xpath("//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href")
    prices = html.xpath("//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em")

    title_list = [str.strip(tt.text_content()) for tt in titles]
    url_list = [u for u in url]
    price_list = [p.text_content() for p in prices]

    results = {'title': title_list, 'price':  price_list, 'url': url_list}
    df = pd.DataFrame(results)
    return df.to_json(force_ascii=False, orient='records').replace('\\', '')

def save(df):
    """
    Function to save a dataframe in data folder (.csv and utf-8 encoding
    """
    df.to_csv('data/mon_csv.csv', encoding="utf-8")

def main():
    pass

if __name__ == '__main__':
    main()
