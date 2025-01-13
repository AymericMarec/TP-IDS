import argparse
from build import build
from check import check
import logging

def IDS():
    
    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    parser = argparse.ArgumentParser(description='pute')

    parser.add_argument('-b', '--build',action='store_true') 
    parser.add_argument('-c', '--check',action='store_true')
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        return
    if(not args.build and not args.check):
        print("Nice argument bro , kys next time")
        parser.print_help()
    if(args.build):
        build()
    if(args.check):
        check()
    
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(format="{levelname}: {message}",style="{",filename='/var/log/ids.log', encoding='utf-8', level=logging.DEBUG)
    IDS()