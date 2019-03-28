# coding:UTF-8 -*-

from lib.get_db import *
from lib.req_url import *
from config.config import *

class Run(object):
    def __init__(self):
        self.db = GetDB()

    def run(self):
        title_dict = get_dict()
        for i in title_dict:
            name = i
            url = title_dict[name]
            if not self.db.check_title(name):
                self.db.add_title(name, url)
        db_title = self.db.check_all()
        logging.info(db_title)

def main():
    Action = Run()
    Action.run()

if __name__ == "__main__":
    main()
