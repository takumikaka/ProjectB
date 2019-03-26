# coding:UTF-8 -*-

from get_db import *

db = GetDB()
db.add_title("古天乐", "123456")
result = db.check_all()
print(result)
