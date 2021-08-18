#!/bin/usr/env python

import requests

import hashlib

import re

req = requests.session()

url  = "http://188.166.173.208:32556/"

###### Realizando GET Request

rget = req.get(url)

###### Salvando a Requisição do GET

html = rget.content

html = html.decode('utf-8')

## print(html)

###### Strip HTML

def html_tags(html):

    clean = re.compile('<.*?>')

    return re.sub(clean, '', html)

## print(html_tags(html))

###### Split String Aleatória

resp = html_tags(html)

resp = resp.split('string')[1]

resp = resp.rstrip()

## print(resp)

###### Encriptando com MD5

mdHash = hashlib.md5(str(resp).encode('utf-8')).hexdigest()

## print(mdHash)

###### Realizando POST Request

data = dict(hash=mdHash)

rpost = req.post(url=url, data=data)

print(rpost.text)
