import argparse
from tumblr_spam_assassin import Findr

parser = argparse.ArgumentParser()
parser.add_argument("apikey")
args = parser.parse_args()

findr = Findr(args.apikey)
spam_blogs = []
popular_tags = ['hamilton', 'jessica jones', 'halloween', 'plants', 'hipster']

for popular_tag in popular_tags:
    spam_blogs.extend(findr.find_spam_blogs(popular_tag))

for spam_blog in spam_blogs:
    print spam_blog

