#-*- coding: utf-8 -*-
import lxml.html
import pandas as pd
import requests
import sqlite3

from sqlalchemy import create_engine

def html_to_dataframe(url_website, titles_xpath, url_xpath, prices_xpath):
    page = requests.get(url_website) 
    html = lxml.html.fromstring(page.content)
    titles = html.xpath(titles_xpath)
    url = html.xpath(url_xpath)
    prices = html.xpath(prices_xpath)

    title_list = [str.strip(tt.text_content()) for tt in titles]
    url_list = [u for u in url]
    price_list = [p.text_content() for p in prices]

    results = {'titles': title_list, 'prices':  price_list, 'url': url_list}
    df = pd.DataFrame(results)
    return df

def save(df):
    engine = create_engine('sqlite:///rakuten.db')
    #df.to_sql('PSP', engine, if_exists='replace')
    df.to_csv('data/mon_csv.csv', encoding="utf-8")

def main():
    df = html_to_dataframe(url_website='http://books.rakuten.co.jp/search/dt?mt=0&o=0&cy=0&h=30&g=006502003001&e=0&v=2&spv=2&s=1&sv=30',\
                           titles_xpath="//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span",\
                           url_xpath="//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href",\
                           prices_xpath="//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em")
    save(df)

if __name__ == '__main__':
     main()
