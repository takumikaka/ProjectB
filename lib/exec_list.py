# -*- coding: utf-8 -*-

import sys
from req_url import *
sys.path.append("..")
from config.config import *

class ExecList(object):
    def __init__(self):
        self.top_urlist = get_top_url()
        self.top_namelist = get_top_name()

    def del_data(self, top_list):
        new_list = []
        for i in range(len(top_list)):
            if i % 2 != 0:
                new_list.append(top_list[i])
        return new_list

    def get_dict(self):
        new_urllist = self.del_data(self.top_urlist)
        new_namelist = self.del_data(self.top_namelist)
        top_dict = dict(zip(new_namelist, new_urllist))
        return top_dict

    def get_magnet(self, movie_list):
        for data in movie_list:
            if "magnet:" in data:
                logging.info(data)
                return data
            else:
                logging.info("数据不存在!")

def main():
    Action = ExecList()
    Action.get_dict()

if __name__ == "__main__":
    main()
