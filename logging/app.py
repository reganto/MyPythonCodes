import logging


logger = logging.getLogger(__name__)

# logging.basicConfig(logging.ERROR, filename='file.log', filemode='a')


f_handler = logging.FileHandler('file.log')
s_handler = logging.StreamHandler()
f_format = logging.Formatter('%(name)s - %(process)s - %(levelname)s - %(message)s')
s_format = logging.Formatter('%(name)s - %(process)s - %(levelname)s - %(message)s')
f_handler.setLevel(logging.ERROR)
s_handler.setLevel(logging.ERROR)
f_handler.setFormatter(f_format)
s_handler.setFormatter(s_format)

logger.critical('This is error message')