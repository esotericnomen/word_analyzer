#! /usr/bin/env python
# coding: utf-8
import urllib2
import html2text

def get_text(url):
	try:
		usock = urllib2.urlopen(url)
		data = usock.read()
		usock.close()
		return html2text.html2text(data)
	except:
		print "error in accessing %s", (url)

if __name__ == "__main__":

	l_url = [
	'http://www.newyorker.com/reporting/2013/11/25/131125fa_fact_bilger',
	'http://www.newyorker.com/',
	'http://en.wikipedia.org/wiki/Wikipedia:Database_download',
	'http://en.wikipedia.org/wiki/Data_corruption'
	]
	
	for url in l_url:
		get_text(url)
