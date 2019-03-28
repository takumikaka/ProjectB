# coding:UTF-8 -*-

import sys
from bs4 import BeautifulSoup
import requests
sys.path.append("..")
from config.config import *

def req_url():
    resp1 = requests.get(url_home)
    resp1.encoding = "gb2312"
    soup = BeautifulSoup(resp1.text, "html.parser")
    return soup

def req_top():
    resp2 = requests.get(url_top)
    resp2.encoding = "gb2312"
    soup = BeautifulSoup(resp2.text, "html.parser")
    return soup

def req_movie(url_movie):
    resp3 = requests.get(url_movie)
    resp3.encoding = "gb2312"
    soup = BeautifulSoup(resp3.text, "html.parser")
    return soup

def get_movie_conlist(url_movie):
    soup = req_movie(url_movie)
    tags_list = list(soup.find(id="text").find_all("p"))
    movie_cont_list = []
    for data in tags_list:
        movie_cont_list.append(data.text)
    return movie_cont_list

def get_movie_title(url_movie):
    movie_cont_list = get_movie_conlist(url_movie)
    movie_title = movie_cont_list[1]
    return movie_title

def get_movie_desc(url_movie):
    movie_cont_list = get_movie_conlist(url_movie)
    movie_desc = movie_cont_list[2]
    return movie_desc

def get_movie_ed2klist(url_movie):
    soup = req_movie(url_movie)
    tags_list = list(soup.find(id="text").find_all("a"))
    movie_magnet_list = []
    for data in tags_list:
        movie_magnet_list.append(data["href"])
    return movie_magnet_list


def get_top_url():
    soup = req_top()
    tags_list = list(soup.find(class_="listBox").find_all("a"))
    top_url_list = []
    for data in tags_list:
        top_url_list.append(data.get("href"))
    return top_url_list

def get_top_name():
    soup = req_top()
    tags_list = list(soup.find(class_="listBox").find_all("a"))
    top_name_list = []
    for data in tags_list:
        top_name_list.append(data.get("title"))
    return top_name_list

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
    return title_dict

def main():
    pass

main()
