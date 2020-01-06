import logging
from logging import handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type": "application/json"}
EMP_ID = 0


def init_logging():
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()

    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='M', interval=1, backupCount=7)

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(sh)
