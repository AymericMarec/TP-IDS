import argparse
from build import build
from check import check

def IDS():
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
    IDS()