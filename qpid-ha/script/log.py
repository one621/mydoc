# coding=utf-8

import logging

class deployLog:
    def __init__(self):
        logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._log = logging.getLogger()
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.INFO)
        #formatter = logging.Formatter("%(filename)s %(message)s")
        #ch.setFormatter(formatter)
        #self._log.addHandler(ch)


LOG = deployLog()

INFO = LOG._log.info
DEBUG = LOG._log.debug
ERROR = LOG._log.error


if __name__ == "__main__":
    INFO("1111111111111")
    DEBUG("22222222222")
    ERROR("3333333333333333")