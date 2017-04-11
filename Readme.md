# Scraping Rakuten.co.jp project

## Description

This package provide an simple REST API when it is install to scrap some data
from rakuten.co.jp web pages.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)

## Install

On you gnome-ubuntu install Python and its libraries::

```sh
  $ sudo apt-get install python-dev
  $ sudo apt-get install virtualenv
  $ virutalenv ~/venv
  $ source ~/venv/bin/activate
  $ git clone <repository-url>
  $ cd scraping
  $ git tag -a 1.0 -m 1.0
  $ pip install -r requirements.txt
  $ pip install . -U
```
## How to use it ?

- Api

When scraping package is install in your virtualenv, open a terminal and run the following script

```sh
  $ scraping-run
```
Then go on the url which is showed on the terminal (http://127.0.0.1:5000/rakutenscraping/api/v1.0/)
You will see some information about route available with the api. 
In particularly, all json data havea field "id". This field allow you to request the api as you want.

For example : http://127.0.0.1:5000/rakutenscraping/api/v1.0/software/keyboardmouse
    Response :
 [
  {
    "description": "You want to by a mouse, this is the right place", 
    "id": "mouse", 
    "url": "http://books.rakuten.co.jp/search/dt?mt=0&o=0&cy=0&h=30&g=004322001&e=0&v=2&spv=2&s=1&sv=30"
  }
 ]

to requesting mouse data : http://127.0.0.1:5000/rakutenscraping/api/v1.0/software/keyboardmouse/mouse
