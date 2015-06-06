#-*- coding: UTF-8 -*-
import logging
import logging.config


#读取logging日志模块的配置文件
logging.config.fileConfig(r"./public/Lt_logging.conf")

LOG = logging.getLogger('handler_hander_users')