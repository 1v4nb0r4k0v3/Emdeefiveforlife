#!/bin/usr/env python

import requests

import hashlib

import re

import os

import sys

if(len(sys.argv)==2):
    
    url = sys.argv[1]

else:

    print("\n-------------------------- ERRO NO PARAMETRO -----------------------\n")
    
    print("Use: " + str(sys.argv[0]) + "http://url:porta")

    exit()

req = requests.session()

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
