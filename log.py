import logging

# logger = logging.getLogger(__name__)
# logging.basicConfig(format="{levelname}: {message}",style="{",filename='/var/log/ids.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger('IDSLogger')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%dT%H:%M:%S")

file_handler = logging.FileHandler('/var/log/ids.log', encoding='utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)