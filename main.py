#! /usr/bin/env python
# coding: utf-8
import urllib2
import sqlite3					# for DB Activities
import html2text
import get_text
import sys
import wikipedia
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

def get_wiki_text(word):
	wiki_page = wikipedia.page(word)
	return wiki_page.summary

def get_meaningful(rword):
	wlen = len(wn.synsets(rword))
	#if rword not in stopwords and wlen is not 0:
	if wlen is not 0:
		entity=(rword,wlen)
		return entity
	else:
	 	return 0
def get_filtered_list(word):
	concordList = []
	for word in html.split():
		#word = str(word)
		word = word.encode('utf-8')
		word = word.translate(None,"0123456789,<>./?;:'\"{[]}\\=+_()*&^%$#@!~`’—-")
		word = word.lower()
		entity = get_meaningful(word);
		if(entity):
			concordList.append(entity)
	return concordList

def add_to_db(concordList,cur):
	for entity in concordList:
		cur.execute("Select * from table_words where word = ?", (entity[0],))
		rword=cur.fetchone()
		if rword is None:
			cur.execute("INSERT INTO table_words VALUES (?,?,?)",(entity[0],1,entity[1]));
		else:
			cur.execute("UPDATE table_words set count = ? where word = ?", (rword[1]+1,entity[0]));
		

if __name__ == "__main__":

	l_url = [
	'http://en.wikipedia.org/wiki/Homomorphic_encryption'
	]

	conn = sqlite3.connect(r"/home/shingu/workspace/word_analyzer/words.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS table_words(word TEXT, count BIGINT, senses INT)")
	
	for url in l_url:
		#html = get_text.get_text(url)
		html = get_wiki_text("Hindu")
		if html:
			concordList = get_filtered_list(html)
			add_to_db(concordList,cur)
			for entity in concordList:

				html = get_wiki_text(entity[0])
				if html:
					concordList1 = get_filtered_list(html)
					add_to_db(concordList1,cur)
	conn.commit()
	conn.close()
	#for entity in concordList:
		#print entity
