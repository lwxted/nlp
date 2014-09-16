import urllib
import pickle
import os
import nltk
import nltk.data
import math
from bs4 import BeautifulSoup
from nltk.stem.lancaster import LancasterStemmer
import operator

st = LancasterStemmer()
document_cnt = 0
ht = {}

for category in os.listdir("./data"):
	path = os.path.join("./data", category)
	if os.path.isdir(path):
		files = os.listdir(path)
		nofiles = len(files)
		for i in xrange(0, nofiles / 2):
			fname = os.path.join(path, str(i) + ".txt")
			with open(fname, "r") as f:
				document_cnt += 1
				appeared_words = set()
				for i in xrange(1, 5):
					f.readline()
				article_ctnt = f.read()
				article_ctnt = article_ctnt.replace(" -- ", " ")
				article_ctnt = article_ctnt.replace(".", "")
				article_ctnt = article_ctnt.replace(",", "")
				article_ctnt = article_ctnt.replace("!", "")
				article_ctnt = article_ctnt.replace("\"", "")
				article_ctnt = article_ctnt.replace("\n", " ")
				article_ctnt = article_ctnt.replace("---", "")
				article_ctnt = article_ctnt.replace("*", " ")
				article_ctnt = article_ctnt.replace("?", " ")
				article_ctnt = article_ctnt.replace("[", " ")
				article_ctnt = article_ctnt.replace("]", " ")
				article_ctnt = article_ctnt.replace(";", " ")
				article_ctnt = article_ctnt.replace("(", " ")
				article_ctnt = article_ctnt.replace(")", " ")
				article_ctnt = article_ctnt.replace("@", " ")
				article_ctnt = article_ctnt.replace("#", " ")
				article_ctnt = article_ctnt.replace(":", " ")
				article_ctnt = article_ctnt.replace("$", " ")
				words = article_ctnt.split(" ")
				for word in words:
					if len(word) > 0 and str.isalpha(word[0]):
						stemmed_word = st.stem(word)
						appeared_words.add(stemmed_word)
				for aword in appeared_words:
					if aword in ht:
						ht[aword] += 1
					else:
						ht[aword] = 1
				f.close()

with open("./idf.txt", "w+") as f:
	sorted_x = sorted(ht.iteritems(), key=operator.itemgetter(0))
	for key, val in sorted_x:
		f.write(key + " " + str(-math.log(float(val) / float(document_cnt))))
		f.write("\n")
	f.close()
