import random

QUOTE_FILE = 'app/static/quotes.txt'

def get_quote():
    line = random.choice(open(QUOTE_FILE).readlines())
    print line
    return line
