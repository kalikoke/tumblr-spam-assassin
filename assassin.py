import argparse
from tumblr_spam_assassin import Findr

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--apikey", type=str)
parser.add_argument("-o", "--output", type=str)
args = parser.parse_args()

findr = Findr(args.apikey, args.output)
findr.find_targets()

