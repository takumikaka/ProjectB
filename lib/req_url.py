# coding:UTF-8 -*-

import sys
from bs4 import BeautifulSoup
import requests
sys.path.append("..")
from config.config import *

def req_url():
    resp2 = requests.get(url)
    resp2.encoding = "gb2312"
    logging.info(resp2.text)
    soup = BeautifulSoup(resp2.text, "html.parser")
    return soup

def get_title_url():
    soup = req_url()
    tags_list = list(soup.find(class_="menutv").find_all("a"))
    data_list = []
    for data in tags_list:
        data_list.append(data["href"])
    return data_list


def get_dict():
    data_list = get_title_url()
    del[data_list[0]]
    title_dict = dict(zip(title_list, data_list))
    logging.info(title_dict)
    return title_dict

def main():
    get_dict()

main()
