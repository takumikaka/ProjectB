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
            logging.info(str(e))
            self.conn.rollback()

    def check_title(self, name):
        result = self.query("select * from title where name = '{0}';".format(name))
        return True if result else False

    def add_title(self, name, url):
        self.exec("insert into title(name, url) values('{0}', '{1}');".format(name, url))

    def check_all(self):
        result = self.query("select * from title;")
