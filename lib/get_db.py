# coding:UTF-8 -*-

import pymysql
import sys
sys.path.append("..")
from config.config import *

class GetDB(object):
    def __init__(self):
        self.conn = pymysql.connect(db_host, db_user, db_passwd, db_table)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logging.error(str(e))
            self.conn.rollback()

    def check_movie(self, name):
        result = self.query("select * from movie where name = '{0}';".format(name))
        return True if result else False

    def check_all(self):
        result = self.query("select * from movie;")
        return result

    def add_movie(self, name, url, title, descp, magnet_url, title_jpg_url, movie_jpg_url):
        self.exec("insert into movie(name, url, title, descp, magnet_url, title_jpg_url, movie_jpg_url) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format(name, url, title, descp, magnet_url, title_jpg_url, movie_jpg_url))
