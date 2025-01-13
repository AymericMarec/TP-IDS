import argparse
from build import build
from check import check
from log import logger

def IDS():
    logger.info("Lancement du script IDS.")
    parser = argparse.ArgumentParser(description='pute')

    parser.add_argument('-b', '--build',action='store_true') 
    parser.add_argument('-c', '--check',action='store_true')
    args = parser.parse_args()
    if(not args.build and not args.check):
        print("Nice argument bro , kys next time")
        parser.print_help()
    if(args.build):
        logger.info("Option --build détectée. Début de la construction.")
        build()
    if(args.check):
        logger.info("Option --check détectée. Début de la vérification.")
        check()
    
if __name__ == "__main__":

    IDS()