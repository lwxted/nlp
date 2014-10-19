#include "sentence.h"
#include <algorithm>

// Helper data structure for keeping original index after sorting.
typedef std::pair<int, int> WordIdPair;
bool comparator (const WordIdPair& left, const WordIdPair& right) {
  return l.first < r.first;
}

Sentence::Sentence() {
  content_.clear();
  byte_length_ = 0;
  sentence_id_ = -1;
  paragraph_pos_ = -1;
}

Sentence::Sentence(const vector<shared_ptr<Word> > content) {
  content_.clear();
  byte_length_ = 0;
  for (int i = 0; i< content.size(); i++) {
	shared_ptr<Word> w = content[i];
	content.push_back(w);
	byte_length_ += w->get_byte_size();	
  }
}

void Sentence::SortContentByDictId() {
  // create a helper storage vector.
  std::sort()
}
