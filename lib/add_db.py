# coding:UTF-8 -*-

from req_url import *
from get_db import *
from exec_list import *
from log_info import *
import sys
sys.path.append("..")
from config.config import *

class AddDB(object):
    def __init__(self):
        self.get_db = GetDB()
        self.exec_list = ExecList()
        self.top_urlist = self.exec_list.del_data(get_top_url())
        self.top_namelist = self.exec_list.del_data(get_top_name())
        self.top_movie_dict = self.exec_list.get_dict()

    def get_movie_cont(self):
        for movie_name in self.top_movie_dict:
            movie_url = self.top_movie_dict[movie_name]
            movie_title = get_movie_title(movie_url)
            movie_desc = get_movie_desc(movie_url)
            movie_magnetlist = get_movie_ed2klist(movie_url)
            movie_magnet = self.exec_list.get_magnet(movie_magnetlist)
            log_info(movie_name, movie_url, movie_title, movie_desc, movie_magnet)
            if not self.get_db.check_movie(movie_name):
                self.get_db.add_movie(movie_name, movie_url, movie_title, movie_desc, movie_magnet)

    def run(self):
        self.get_movie_cont()
        #result = self.get_db.check_all()
        #logging.info(result)
