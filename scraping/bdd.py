#-*- coding: utf-8 -*-

games = [
    {
        'id': u'3DS',
        'title': u'Nintendo 3DS',
        'description': u'A lot of product in relation with Nitendo 3DS from rakuten.co.jp',
        'done': False
    }
]

nintendo3DS = [
    {
        'id': u'device',
        'description': u'You want to by a 3DS, this is the right place',
        'url': 'http://books.rakuten.co.jp/search/dt/g006508001/',
        'titles_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span",
        'url_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href",
        'prices_xpath': "//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em",
        'done': False
    },
    {
        'id': u'component',
        'description': u'Here you can find additional component for nintendo 3DS',
        'url': 'http://books.rakuten.co.jp/search/dt?mt=0&o=0&cy=0&h=30&g=006508002&e=0&v=2&spv=2&s=1&sv=30',
        'titles_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/span",
        'url_xpath': "//div[@class='rbcomp__item-list__item__details__lead']/h3/a/@href",
        'prices_xpath': "//div[@class='rbcomp__item-list__item__details__info__main']/p[@class='rbcomp__price']/span/em",
        'done': False
    }
]

