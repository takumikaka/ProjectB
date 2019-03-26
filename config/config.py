# coding:UTF-8 -*-

import os
import logging

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_file = os.path.join(prj_path, "log", "log.txt")

url = "http://www.6vhao.tv"

title_list = ["喜剧片", "动作片", "爱情片", "恐怖片", "科幻片", "战争片", "纪录片", "故事片", "动画片", "国剧", "日韩剧", "欧美剧", "3D电影", "综艺"]

header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
          "Accept-Encoding": "gzip, deflate",
          "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
          "Cache-Control": "max-age=0",
          "Connection": "keep-alive",
          "Host": "www.6vhao.tv",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}

logging.basicConfig(level = logging.DEBUG,
                   format = "[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s %(lineno)d] %(message)s",
                   datefmt = "%Y-%m-%d %H: %M: %S",
                   filename = log_file,
                   filemode = "a")

db_host = "localhost"
db_user = "root"
db_passwd = "Raspberry2019"
db_table = "6vhao_db"
table_title = "title"
