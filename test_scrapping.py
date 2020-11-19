import requests
from bs4 import BeautifulSoup

# !/usr/bin/python3
# -*- coding:utf8 -*-

""" - INFORMATION FICHIER - """

"""
Projet de Discrimination - Test de Scrapping
fichier  : test_scrapping.py
@author : MONFRET Dylan
"""

""" - VARIABLES GLOBALES - """

url_base_players = "https://sofifa.com/team/"

""" - DEFINITION DE FONCTION LOCALE - """


def get_url_text(url_raw):
    source_code = requests.get(url_raw)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    return soup


""" - PRE-TRAITEMENTS - """

""" - CORPS PRINCIPAL - """
