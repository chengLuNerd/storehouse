import logging


logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='parser_result.log',
                    filemode='w')

logging.debug('debug msg')
logging.info('info msg')
logging.warning('warn msg')
logging.error('error msg')
logging.critical('critical msg')
