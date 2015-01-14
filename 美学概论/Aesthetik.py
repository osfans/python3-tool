#!/usr/bin/env python3
"""抓美学概论的博文"""

from bs4 import BeautifulSoup
import re
import urllib.request

def get(url):
	f = urllib.request.urlopen(url)
	cont = f.read().decode("utf-8")
	f.close()
	cont = re.findall("<body>.*</body>", cont, re.DOTALL)[0]
	tree = BeautifulSoup(cont, "html.parser")
	return tree

def getCont(url):
	tree = get(url)
	title  = tree.find("h2")
	body = tree.find("div", {"id":"sina_keyword_ad_area2"})
	return "%s\n%s\n" % (title, body)

head = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>美学概论_独孤飞狐_新浪博客</title>
</head>
<body>"""

tree = get("http://blog.sina.com.cn/s/articlelist_1219523914_1_1.html")
soups = tree(None, {"class":"atc_title"})
soups.reverse()
print(head)
for i in soups:
	if '美学' in i.text:
		print(getCont(i.a['href']).replace("real_src", "src"))
print("</body></html>")
