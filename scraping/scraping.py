#-*- coding: utf-8 -*-
import lxml.html
import pandas as pd
import requests

def get_game_data(url_website, titles_xpath, url_xpath, prices_xpath):
    """
    Function to return game product sold on rakuten
    """
    page = requests.get(url_website) 
    html = lxml.html.fromstring(page.content)
    titles = html.xpath(titles_xpath)
    url = html.xpath(url_xpath)
    prices = html.xpath(prices_xpath)

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
    df = get_game_data(url_website='http://books.rakuten.co.jp/search/dt?mt=0&o=0&cy=0&h=30&g=006502003001&e=0&v=2&spv=2&s=1&sv=30',\
                           titles_xpath="//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span",\
                           url_xpath="//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href",\
                           prices_xpath="//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em")
    save(df)

if __name__ == '__main__':
    main()
