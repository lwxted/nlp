import os
import nltk
import pickle
import nltk.data
import math
from nltk.stem.lancaster import LancasterStemmer
"more docs."
data_path = "./data/"
raw_path = "./raw/"

st = LancasterStemmer()


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)

links = load_obj("link_dic")
for category, item in links.iteritems():
	for obj in item:
		print obj[1]

# Preprocess all files to adapt to required format
"""
def process_text(s):
	s = s.replace(' -- ', ' ')
	s = ''.join(c for c in s if c == ' ' or c == '\'' or c == '-' or c == '\n' or c.isalnum())
	s = s.lower()
	ans = ''
	arr = s.split(' ')
	for i in xrange(0, len(arr)):
		ans += st.stem(arr[i])
		if i != len(arr) - 1:
			ans += ' '
	return ans

for category_folder_name in os.listdir(data_path):
	category_path = os.path.join(data_path, category_folder_name)
	if os.path.isdir(category_path):
		number_of_files = len(os.listdir(category_path))
		for i in xrange(0, number_of_files / 2):
			title = ''
			ctnt = ''
			tmpctnt = ''
			with open(os.path.join(category_path, str(i) + ".txt"), "r") as f:
				f.readline()
				title = process_text(f.readline()[7:])
				f.readline()
				f.readline()
				ctnt = process_text(f.read())
				f.close()
			with open(os.path.join(category_path, str(i) + ".txt"), "w") as f:
				f.write(title)
				f.write(ctnt)
				f.close()
			with open(os.path.join(category_path, str(i) + "h.txt"), "r") as f:
				tmpctnt = f.read().replace('\n', ' ')
				tmpctnt = process_text(tmpctnt)
				f.close()
			with open(os.path.join(category_path, str(i) + "h.txt"), "w") as f:
				f.write(tmpctnt)
				f.close()
"""

# Format data for Sam
"""
no_words = 1
document_cnt = 0
WORD_INDEX_TABLE = {}
WORD_TF_CNT = {}

for category_folder_name in os.listdir(data_path):
	category_path = os.path.join(data_path, category_folder_name)
	if os.path.isdir(category_path):
		number_of_files = len(os.listdir(category_path))
		category_raw_path = os.path.join(raw_path, category_folder_name)
		if not os.path.exists(category_raw_path):
			os.makedirs(category_raw_path)
		for i in xrange(0, number_of_files / 2):
			_COST = ''
			_TEXT_PROC = ''
			_WORDS = ''
			_M_WORDS = ''
			document_cnt += 1
			with open(os.path.join(category_path, str(i) + ".txt"), "r") as f:
				ctnt = f.read()
				_TEXT_PROC = ctnt
				arr = ctnt.split('\n')
				ST = set()
				sentence_index = 0
				for sentence in arr:
					sentence_index += 1
					_COST += str(len(sentence)) + '\n'
					words_in_sentence = sentence.replace('\n', '').split(' ')
					word_index = 0
					for word in words_in_sentence:
						if len(word) > 0 and word != ' ' and word != '':
							# Not empty word
							word_index += 1
							if word not in WORD_INDEX_TABLE:
								WORD_INDEX_TABLE[word] = no_words
								no_words += 1
							ST.add(WORD_INDEX_TABLE[word])
							_WORDS += str(sentence_index) + ' ' + str(word_index) + ' ' + str(WORD_INDEX_TABLE[word]) + '\n'
				for word in ST:
					if word not in WORD_TF_CNT:
						WORD_TF_CNT[word] = 1
					else:
						WORD_TF_CNT[word] += 1
				f.close()
			with open(os.path.join(category_path, str(i) + "h.txt"), "r") as fh:
				ctnt = fh.read().replace('\n', '')
				arr = ctnt.split(' ')
				word_index = 0
				for word in arr:
					if len(word) > 0 and word != ' ' and word != '':
						word_index += 1
						if word not in WORD_INDEX_TABLE:
							WORD_INDEX_TABLE[word] = no_words
							no_words += 1
						_M_WORDS += '1 ' + str(word_index) + ' ' + str(WORD_INDEX_TABLE[word]) + '\n'
				f.close()
			with open(os.path.join(category_raw_path, str(i) + ".txt.proc"), "w+") as f_txt_proc:
				f_txt_proc.write(_TEXT_PROC)
				f_txt_proc.close()
			with open(os.path.join(category_raw_path, str(i) + ".cost"), "w+") as f_cost:
				f_cost.write(_COST)
				f_cost.close()
			with open(os.path.join(category_raw_path, str(i) + ".m.words"), "w+") as f_m_words:
				f_m_words.write(_M_WORDS)
				f_m_words.close()
			with open(os.path.join(category_raw_path, str(i) + ".words"), "w+") as f_words:
				f_words.write(_WORDS)
				f_words.close()

save_obj(WORD_INDEX_TABLE, "WORD_INDEX_TABLE")
"""

# Output dictionary
"""
WORD_INDEX_TABLE = load_obj("WORD_INDEX_TABLE")
WORD_INDEX_TABLE_HT = {}

for key, val in WORD_INDEX_TABLE.iteritems():
	WORD_INDEX_TABLE_HT[val] = key
with open('./dict', 'w+') as f:
	for key, val in WORD_INDEX_TABLE_HT.iteritems():
		f.write(str(key) + ' ' + str(val) + '\n')
	f.close()
"""

# IDF
"""
data_standardized_path = './data_standardized/'
WORD_TF_CNT = {}

document_cnt = 0

for category_folder_name in os.listdir(data_standardized_path):
	category_path = os.path.join(data_standardized_path, category_folder_name)
	if os.path.isdir(category_path):
		number_of_files = len(os.listdir(category_path))
		for i in xrange(0, number_of_files / 4):
			p = os.path.join(category_path, str(i) + ".words")
			if os.path.exists(p):
				# print p
				with open(p, "r") as f:
					document_cnt += 1
					ST = set()
					for line in f:
						word = int(line.split(' ')[-1])
						ST.add(word)
					for word in ST:
						if word not in WORD_TF_CNT:
							WORD_TF_CNT[word] = 1
						else:
							WORD_TF_CNT[word] += 1
					f.close()

			p_ref = os.path.join(category_path, str(i) + ".m.words")
			if os.path.exists(p_ref):
				# print p
				with open(p_ref, "r") as f:
					document_cnt += 1
					ST = set()
					for line in f:
						word = int(line.split(' ')[-1])
						ST.add(word)
					for word in ST:
						if word not in WORD_TF_CNT:
							WORD_TF_CNT[word] = 1
						else:
							WORD_TF_CNT[word] += 1
					f.close()

with open('./idf', 'w+') as f:
	for key, val in WORD_TF_CNT.iteritems():
		idf = -math.log(float(val) / float(document_cnt))
		if math.fabs(idf) < .0000001:
			idf = 0.
		f.write(str(key) + ' ' + str(idf) + '\n')
	f.close()
"""

# Fix the cost count
"""
raw_data_path = './raw_data_crawled_from_cnn/'
data_standardized_path = './data_standardized/'

for category_folder_name in os.listdir(data_standardized_path):
	category_path = os.path.join(data_standardized_path, category_folder_name)
	rpath = os.path.join(raw_data_path, category_folder_name)
	if os.path.isdir(rpath):
		number_of_files = len(os.listdir(rpath))
		for i in xrange(0, number_of_files / 2):
			_COST = ''
			_TEXT = ''
			with open(os.path.join(rpath, str(i) + ".txt"), "r") as f:
				f.readline()
				title = f.readline()[7:-1]
				_TEXT += title + '\n'
				_COST += str(len(title)) + '\n'
				f.readline()
				f.readline()
				arr = f.read().split('\n')
				for sentence in arr:
					_TEXT += sentence + '\n'
					_COST += str(len(sentence)) + '\n'
				f.close()
			with open(os.path.join(category_path, str(i) + ".txt"), "w+") as f:
				f.write(_TEXT)
				f.close()
			with open(os.path.join(category_path, str(i) + ".cost"), "w+") as f:
				f.write(_COST)
				f.close()
"""
