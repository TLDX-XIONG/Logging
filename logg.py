import logging
import logging.config as log_config
from logging import StreamHandler
from logging import FileHandler


# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s[line:%(lineno)s] %(levelname)s %(name)s %(message)s',
#     datefmt='%a, %d %b %Y %H:%M:%S',
#     filename='test.log', 
#     filemode='a', )


# logger = logging.getLogger(__name__)

# # 设置为DEBUG级别
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter(
#     fmt='%(asctime)s %(filename)s[line:%(lineno)s] %(levelname)s %(name)s %(message)s', 
#     datefmt='%a, %d %b %Y %H:%M:%S')

# # 标准流处理器，设置的级别为WARAING
# stream_handler = StreamHandler()
# stream_handler.setLevel(logging.WARNING)
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)

# # 文件处理器，设置的级别为INFO
# file_handler = FileHandler(filename="test.log")
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# logger.debug("this is debug")
# logger.info("this is info")
# logger.error("this is error")
# logger.warning("this is warning")
# logger.critical('this is critical')



log_config.fileConfig('logging.conf')

# 创建 logger
logger = logging.getLogger()

# 应用代码
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
