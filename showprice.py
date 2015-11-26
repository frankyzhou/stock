# -*- coding:cp936 -*-
from pylab import *
from matplotlib.dates import DateFormatter, WeekdayLocator, HourLocator, \
DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
plot_day_summary, candlestick2
from matplotlib.font_manager import FontProperties


font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=18)
mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')

def showStock(stock_num,date1,date2):
	# define the code number and begin end date
	# date1 = ( 2012, 12, 25 )
	# date2 = ( 2013, 6, 1 )
	# stock_num = '000651.sz'
	# define date format
	# get the stock data
	quotes = quotes_historical_yahoo(stock_num, date1, date2)
	if len(quotes) == 0:
		raise SystemExit
	# draw k line of stock
	fig = figure()
	fig.subplots_adjust(bottom=0.2)
	ax = fig.add_subplot(111)
	ax.xaxis.set_major_locator(mondays)
	ax.xaxis.set_minor_locator(alldays)
	ax.xaxis.set_major_formatter(weekFormatter)
	candlestick(ax, quotes, width=0.6)
	# plot_day_summary(ax, quotes, ticksize=3)
	ax.xaxis_date()
	ax.autoscale_view()
	setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')
	title(u'2012,12,25-2013,6,1',fontproperties=font)
	show()


def showEmotion(emotionList):
	fig = figure()
	fig.subplots_adjust(bottom=0.2)
	axes = fig.add_subplot(111)
	dateList = []
	yList = []
	for key in sorted(emotionList.keys()):
		Y = int(key[0:4])
		M = int(key[5:7])
		D = int(key[8:10])
		# print Y,M,D
		date = datetime.datetime(Y,M,D)
		dateList.append(date)
		yList.append(emotionList[key])
	# print len(dateList)
	axes.plot_date(dateList,  yList,  'm-',  marker='.',  linewidth=1)
	axes.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d') )
	axes.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
	# fig.autofmt_xdate()
	show()

# showStock("600110.sh",(2012,12,10),(2013,6,1))
# emotionList = {}
# emotionList["2010-01-01"] = 1
# emotionList["2014-02-10"] = 1
# showEmotion(emotionList)