# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from config.config import *

def log_info(name, url, title, desc, magnet, title_jpg, movie_jpg):
    logging.info("电影名: {0}".format(name))
    logging.info("电影链接: {0}".format(url))
    logging.info("电影信息: {0}".format(title))
    logging.info("电影简介: {0}".format(desc))
    logging.info("磁链接: {0}".format(magnet))
    logging.info("标题图片: {0}".format(title_jpg))
    logging.info("电影图片: {0}".format(movie_jpg))
