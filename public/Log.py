import logging
import os
import time
from get_config import config
from logging import handlers



class Logs():
    def __init__(self):
        log_path = config().get_log("teach_log")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        self.file_name = os.path.join(log_path,"%s.log" % time.strftime("%Y_%m_%d")) # 生成log日志路径
        self.formatter = logging.Formatter("%(asctime)s-%(filename)s [line:%(lineno)d]-%(levelname)s:%(message)s")  # 设置输出格式


    def my_log(self,level,message):
        logger = logging.getLogger()    # 创建一个logger对象
        logger.setLevel(logging.INFO)   # 设置log的等级开关

        str_handler = logging.StreamHandler()  # 设置handler，用于输出到控制台
        str_handler.setLevel(logging.WARNING)  # 为输出的日志设置等级

        tf_handle = handlers.TimedRotatingFileHandler(filename=self.file_name,interval= 1, when="D",encoding="utf8")    # 按天分割日志
        tf_handle.setFormatter(self.formatter)
        logger.addHandler(tf_handle)

        # handler = logging.FileHandler(self.file_name,mode= "a",encoding= "utf-8")    # 打开日志文件进行追加日志
        # handler.setLevel(logging.DEBUG) # 为输入日志设置等级
        # handler.setFormatter(self.formatter)
        # logger.addHandler(handler)

        logger.addHandler(str_handler)
        str_handler.setFormatter(self.formatter)

        if level == "info":
            logging.info(message)
        elif level == "debug":
            logging.debug(message)
        elif level == "error":
            logging.error(message)
        elif level == "warning":
            logging.warning(message)

        logger.removeHandler(str_handler)
        logger.handlers.pop()
        logging.shutdown()
        # logger.removeHandler(handler)




# class write_log():
#
#     log_path = config().get_log("teach_log")
#     if not os.path.exists(log_path):
#         os.makedirs(log_path)
#
#     file_name = os.path.join(log_path, "%s.log" % time.strftime("%Y_%m_%d")) # 生成log日志路径
#     logging.basicConfig(filename = file_name,
#                             filemode= "a",
#                             format = "%(asctime)s-%(filename)s [line:%(lineno)d]-%(levelname)s:%(message)s",
#                             level= logging.INFO)    # 只记录日志，不输出到控制台，设置日志属性
#
#
#     def log_info(self,message):
#         # 运行日志
#         if message != [] or message != {} or message != "":
#             logging.info(str(message))
#         else:
#             pass
#
#     def log_error(self,message):
#         # 错误日志
#         if message != [] or message != {} or message != "":
#             logging.error(str(message))
#         else:
#             pass



if __name__ == '__main__':
    # a = write_log()
    # a.log_error("This is run error,错误日志")
    # l = Logs()
    Logs().my_log("error","我是测试数据拉拉啦")


