import urllib
import pickle
import os
import nltk
import nltk.data
from bs4 import BeautifulSoup


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)

def save_to_file(category, cnt, title, link, main_ctnt, highlight_ctnt):
	folder_path = "./data/" + category + "/"
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
	with open(folder_path + str(cnt) + ".txt", 'w+') as f:
		f.write("CATEGORY: " + category + "\n")
		f.write("TITLE: " + title + "\n")
		f.write("LINK: " + link + "\n\n")
		f.write(main_ctnt)
		f.close()
	with open(folder_path + str(cnt) + "h.txt", 'w+') as f:
		f.write(highlight_ctnt)
		f.close()

# link_dic = {}
# Get all RSS title + link and save to local pickle.
# for title, html in load_obj("rss_dic").iteritems():
# 	link_dic[title] = []
# 	crawler = urllib.urlopen(html)
# 	rawcnt = crawler.read()
# 	# print rawcnt
# 	parser = BeautifulSoup(rawcnt)
# 	itms = parser.find_all("item")
# 	for item in itms:
# 		link_dic[title].append((item.find("title").getText(), item.find("guid").getText()))
# 	save_obj(link_dic, "link_dic")

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
link_dic = load_obj("link_dic")
for category, itms in link_dic.iteritems():
	cnt = 0
	for title, link in itms:
		try:
			crawler = urllib.urlopen(link)
			rawcnt = crawler.read()
			parser = BeautifulSoup(rawcnt)
			maincnt = ""
			highlightcnt = ""
			for p in parser.find_all("p"):
				maincnt += p.getText().encode('utf-8').strip() + " "
			highlight = parser.find(class_ = "cnnStryHghLght")
			if hasattr(highlight, "find_all"):
				for li in highlight.find_all("li"):
					highlightcnt += li.getText().encode('utf-8').strip() + "\n"
				maincnt = maincnt.replace("\"", "")
				maincnt = maincnt.replace("'s", "^s")
				maincnt = maincnt.replace("'d", "^d")
				maincnt = maincnt.replace("'ve", "^ve")
				maincnt = maincnt.replace("'re", "^re")
				maincnt = maincnt.replace("'m", "^m")
				maincnt = maincnt.replace("'", "")
				maincnt = maincnt.replace("^s","'s")
				maincnt = maincnt.replace("^d","'d")
				maincnt = maincnt.replace("^ve","'ve")
				maincnt = maincnt.replace("^re","'re")
				maincnt = maincnt.replace("^m","'m")
				maincnt = '\n'.join(sent_detector.tokenize(maincnt.strip()))
				save_to_file(category, cnt, title, link, maincnt, highlightcnt)
				cnt += 1
				print category, cnt, title
		except Exception, e:
			print "Exception: " + str(e)