"""Get some stock market prices data."""
from time import ctime
from urllib2 import urlopen

companies = (
    'goog', 'aapl', 'yhoo', 'ibm', 'cost', 'adbe', 'intc',
    'wmt', 'msft', 'lee', 'hpq', 'v', 'dis')
url = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'

print '\n Prices quoted as of: {} PDT \n'.format(ctime())
print 'COMP', 'PRICE', 'CHANGE', '%AGE'
print '-----', '-----', '-----', '-----'

# get the url content data from yahoo service
data = urlopen(url % ','.join(companies))
for row in data:
    company, price, chg, per = row.split(',')
    if isinstance(price, str):
        print company, price, chg, per,
    else:
        print company, '%.2f' % float(price), chg, per,

data.close()
