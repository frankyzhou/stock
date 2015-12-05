#encoding=utf-8

# others
import xlrd
from pyExcelerator import *
import jieba
# personal
import dict
import util
import showprice
#import test_svm

def calEmotion(filename,city):
	# load dict
	most,very,more,insuff,ish,posdict,negdict,over=dict.init_dict()
	jieba.load_userdict("dic/stock_dict.txt")
	# init score
	score = {}
	cur_date = 0
	review_id =0
	#init excel hander
	w, ws = createExcel()
	# open database & get data
	rawdata, conn, cur = util.getData(filename,city)
	for row in rawdata:
		# collect tokens from yield
		seg_list,cur_date, review = getTokens(score,row,cur_date)
		#use sentiment score to cal the emotion by one comment and add it to score.	
		result = dict.sentiment_score_list(seg_list,posdict,negdict,most,very,more,ish,insuff,over)
		score[cur_date].append(result)
		# write down the review to xls
		review_id = review_id +1
		ws.write(review_id,0,review)
		ws.write(review_id,1,result)
	w.save("excel/" + filename + ".xls")
	# close the connection with database
	util.closeDB(conn, cur)
	# generate the emotionlist from score
	emotionList = genEmotionList(score)
	# show pic of the stock price and emotion by one stock
	showPriceAndEmotion(emotionList,filename,city)

def getTokens(score,row,cur_date):
	date = row[0].split(' ')[0]
	if date != cur_date: 
		cur_date = date
		score[cur_date] = []

	review = row[3].split('#')[1]
	seg_gen = jieba.cut(review)
	seg_list = []
	for key in seg_gen: seg_list.append(key) 
	return seg_list, cur_date, review

def createExcel():
	w = Workbook()     #创建一个工作簿
	ws = w.add_sheet("sheet1")     #创建一个工作表
	ws.write(0,0,u'\u59D3\u540D')
	return w,ws

def genEmotionList(score):
	emotionList = {}
	for date in score:
		emotionList[date] = util.avgList(score[date])
	return emotionList

def showPriceAndEmotion(emotionList,filename,city):
	showprice.showEmotion(emotionList)
	showprice.showStock(filename+"."+city,(2012,12,23),(2013,6,7))


calEmotion("000651","sz")
