// This header file defines the sentence primitive (article-specific).
// Author: Jiaji Zhou
// We choose not to contain feature vectors since these primitives (word, sentence)
// should be able to be initialized from raw json files at the very first stage. 
// Feature Processing is performed after primitives are constructed.

#include "word.h"
#include <vector>

class Sentence {
 public:
  Sentence();
  Sentence(const vector<shared_ptr<Word> >& content);
  void AppendWord(const Word& w);
  
 private:
  // Sentence Id within the article.
  int sentence_id_;
  
  // Sentence Position within the paragraph.
  int paragraph_pos_;  

  // Vector of words in original written order.
  // Use shared_ptr to avoid value copy. There should be a global dictionary
  // constructed beforehand and every usage of word is an address reference 
  // as in shared_ptr here.
  vector<shared_ptr<Word> > content_;

  // Vector of words sorted by dictionary id for easy inner product/overlapping
  // computation among sentences. Use a vector for reindexing.
  vector<int> ordered_index;
  // Sentence length.
  int byte_length_;
  void SortContentByDictId();
};
