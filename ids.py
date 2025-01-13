import argparse

parser = argparse.ArgumentParser(description='pute')

parser.add_argument('-b', '--build',action='store_true') 
parser.add_argument('-c', '--check',action='store_true')

args = parser.parse_args()
print(args.build,args.check)