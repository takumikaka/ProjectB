# -*- coding: utf-8 -*-

import threading
import sys
import time
sys.path.append("..")
from config.config import *
from lib.add_db import *

add_db = AddDB()

def Tic():
    add_db.run()
    global timer
    timer = threading.Timer(36000, Tic)
    #timer = threading.Timer(5, Tic)
    timer.start()

timer = threading.Timer(1, Tic)
timer.start()
