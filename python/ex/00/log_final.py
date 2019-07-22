import logging

logger = logging.getLogger('simple_example')
# 打印logger的名称
print(logger.name)

# 设置logger的日志级别
logger.setLevel(logging.DEBUG)

# 创建两个handler，一个负责将日志输出到终端，一个负责输出到文件，并分别设置它们的级别
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler(filename="simple.log", mode="w")
fh.setLevel(logging.WARNING)
# 创建一个格式化器，用于handler上
formatter =  logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 设置两个handler的格式化器
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 为logger添加两个handler
logger.addHandler(ch)
logger.addHandler(fh)

#记录日志
logger.debug('debug msg')
logger.info('info msg')
logger.warning('warn msg')
logger.error('error msg')
logger.critical('critical msg')
