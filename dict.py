
#encoding=utf-8
def judgeodd(num):
    if (num/2)*2 == num:
        return 'even'
    else:
        return 'odd'
				
def init_dict():
		fmost = open('d:/src/dic/mostdict.txt','r')
		fvery = open('d:/src/dic/verydict.txt','r')
		fmore = open('d:/src/dic/moredict.txt','r')
		fish = open('d:/src/dic/ishdict.txt','r')
		finsuff = open('d:/src/dic/insufficientlydict.txt','r')

		most = []
		very = []
		more = []
		ish  = []
		insuff = []
		over = []
		posdict = []
		negdict = []

		for line in fmost : most.append(line.strip().decode('gbk'))
		for line in fvery : very.append(line.strip().decode('gbk'))
		for line in fmore : more.append(line.strip().decode('gbk'))
		for line in fish : ish.append(line.strip().decode('gbk'))
		for line in finsuff : insuff.append(line.strip().decode('gbk'))

		finsuff.close()
		fmost.close()
		fvery.close()
		fish.close()
		fmore.close()

		fover = open('d:/src/dic/overdict.txt','r')
		fpos  = open('d:/src/dic/posdict.txt','r')
		fneg  = open('d:/src/dic/negdict.txt','r')
		for line in fover : over.append(line.strip().decode('gbk'))
		for line in fpos : posdict.append(line.strip().decode('gbk'))
		for line in fneg : negdict.append(line.strip().decode('gbk'))
		fover.close()
		fpos.close()
		fneg.close()		
		return most,very,more,insuff,ish,posdict,negdict,over

def sentiment_score_list(dataset,posdict,negdict,mostdict,verydict,moredict,ishdict,insufficientdict,inversedict):
		cuted_data = dataset
		count1 = 0
		count2 = []
		
		for word in cuted_data: #循环遍历每一个评论
				#print word
				i = 0 #记录扫描到的词的位置
				a = 0 #记录情感词的位置
				poscount = 0 #积极词的第一次分值
				poscount2 = 0 #积极词反转后的分值
				poscount3 = 0 #积极词的最后分值（包括叹号的分值）
				negcount = 0
				negcount2 = 0
				negcount3 = 0
				if word in posdict: #判断词语是否是情感词
						# print word
						poscount += 1                
						c = 0
						for w in cuted_data[a:i]:  #扫描情感词前的程度词
								if w in mostdict:
										poscount *= 4.0
								elif w in verydict:
										poscount *= 3.0
								elif w in moredict:
										poscount *= 2.0
								elif w in ishdict:
										poscount /= 2.0
								elif w in insufficientdict:
										poscount /= 4.0
								elif w in inversedict:
										c += 1
						# if judgeodd(c) == 'odd': #扫描情感词前的否定词数
						# 		poscount *= -1.0
						# 		poscount2 += poscount
						# 		poscount = 0
						# 		poscount3 = poscount + poscount2 + poscount3
						# 		poscount2 = 0
						# else:
						# 		poscount3 = poscount + poscount2 + poscount3
						# 		poscount = 0
						a = i + 1 #情感词的位置变化,之前的范围不算

				elif word in negdict: #消极情感的分析，与上面一致
						# print word
						negcount += 1
						d = 0
						for w in cuted_data[a:i]:
								if w in mostdict:
										negcount *= 4.0
								elif w in verydict:
										negcount *= 3.0
								elif w in moredict:
										negcount *= 2.0
								elif w in ishdict:
										negcount /= 2.0
								elif w in insufficientdict:
										negcount /= 4.0
								elif w in inversedict:
										d += 1
								if judgeodd(d) == 'odd':
										negcount *= -1.0
										negcount2 += negcount
										negcount = 0
										negcount3 = negcount + negcount2 + negcount3
										negcount2 = 0
								else:
										negcount3 = negcount + negcount2 + negcount3
										negcount = 0
						a = i + 1
				# elif word == '！'.decode('utf-8') or word == '!': ##判断句子是否有感叹号
						# for w2 in cuted_data[::-1]: #扫描感叹号前的情感词，发现后权值+2，然后退出循环
								# if w2 in posdict or negdict:
										# poscount3 += 2
										# negcount3 += 2
										# break                    
				i += 1 #扫描词位置前移

	  #以下是防止出现负数的情况
		# pos_count = 0
		# neg_count = 0
		# if poscount3 < 0 and negcount3 > 0:
				# neg_count += negcount3 - poscount3
				# pos_count = 0
		# elif negcount3 < 0 and poscount3 > 0:
				# pos_count = poscount3 - negcount3
				# neg_count = 0
		# elif poscount3 < 0 and negcount3 < 0:
				# neg_count = -poscount3
				# pos_count = -negcount3
		# else:
				# pos_count = poscount3
				# neg_count = negcount3

				count1 += (poscount-negcount)
				#if count1 != [[0, : print count1
				#count2.append(count1)
				#count1 = []    
		return count1