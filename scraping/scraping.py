#-*- coding: utf-8 -*-
import lxml.html
import pandas as pd
import requests


if __name__ == '__main__':
    url = 'http://books.rakuten.co.jp/search/dt/g006502003/?&v=2&spv=2'
    page = requests.get(url)
    html = lxml.html.fromstring(page.content)
    titles = html.xpath("//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span")
    url = html.xpath("//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href")
    prices = html.xpath("//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em")

    title_list = [tt.text_content() for tt in titles]
    url_list = [u for u in url_products]
    price_list = [p.text_content() for p in prices]

    results = {'titles': title_list, 'prices':  price_list, 'url': url_list}
    df = pd.DataFrame(results)
    #main()
