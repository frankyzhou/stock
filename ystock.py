import ystockquote  as ys
from pprint import pprint  
#print ystockquote.get_price('002250.sz')  
#print ystockquote.get_all('002250.sz')  
  
# a =  ys.get_historical_prices('000651.sz','2012-12-01','2012-12-31')
# #pprint (ys.get_historical_prices('002250.sz','2010-01-01','2010-01-11'))
# akey = a.keys()
# akey = list(akey)
# akey.sort()
# for k in akey: print k,a[k]['Close']
def compPrice(date,num,city):
	ys.get_historical_prices('000651.sz',date,)