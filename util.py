import sqlite3

def avgList(arraylist):
	sum = 0
	for e in arraylist:
		sum = sum + e
	return  float(sum) / len(arraylist)

# get data from the database and return conn & cur
def getData(filename,city):
	#absolute path instead of relative path 
	conn = sqlite3.connect("d:/src/stock/db/CLICK"+filename+".db")
	cur =conn.cursor()
	sql = "SELECT date,click,reply,title FROM click"+ filename +" order by date"
	return cur.execute(sql),conn,cur
	#get all table in the db file
	# for row in cur.execute("""SELECT name FROM sqlite_master
	# WHERE type='table'
	# ORDER BY name;"""):
	    # print row


	#get all column in the db file
	# for row in cur.execute("""
	# SELECT sql FROM sqlite_master 
	# WHERE type="table" AND name = "click000651"
	# """):
	    # print row		
	#date text, click int, reply int, title text

def closeDB(conn,cur):
	conn.commit()
	cur.close()
	conn.close()