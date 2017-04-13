# Scraping Rakuten.co.jp project

## Description

This package provide an simple REST API when it is install to scrap some data
from rakuten.co.jp web pages.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)

## Install

On you gnome-ubuntu install Python and its libraries (works with Python3 and Python2):

```sh
  $ sudo apt-get install python-dev
  $ sudo apt-get install virtualenv
  $ virtualenv ~/venv
  $ source ~/venv/bin/activate
  $ git clone <repository-url>
  $ cd scraping
  $ make requirements
  $ make psi
```
## How to use it ?

- Api

When scraping package is install in your virtualenv, open a terminal and run the following script

```sh
  $ scraping-run
```
Then go on the url showed on your terminal (http://127.0.0.1:5000)
You will see some information about route available with the api. 
In particularly, all json data have a field "id". This field allow you to request the api as you want.

For example : http://127.0.0.1:5000/rakutenscraping/api/v1.0/software/keyboardmouse
    Response :
```json
 [
  {
    "description": "You want to by a mouse, this is the right place", 
    "id": "mouse", 
    "url": "http://books.rakuten.co.jp/search/dt?mt=0&o=0&cy=0&h=30&g=004322001&e=0&v=2&spv=2&s=1&sv=30"
  }
 ]
```
to requesting mouse data : http://127.0.0.1:5000/rakutenscraping/api/v1.0/software/keyboardmouse/mouse

- Data

All data provided by the API is in json format. With request package in python you can load the content
in a dataframe with the script below

```py
    import pandas as pd
    import requests

    data = requests.get('http://127.0.0.1:5000/rakutenscraping/api/v1.0/software/keyboardmouse/mouse')
    df = pd.read_json(data.json())
```
