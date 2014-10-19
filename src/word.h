// This header file defines the word primitive. 
// Author: Jiaji Zhou  
// Word class is meant to be global rather than dependent on specific
// sentence or article.
// Word may have more attributes like LanguangeType, weight, etc.

#include <string>
#include <stdio.h>

class Word {
 public:
  Word() {
	name_ = " ";
	dict_id_ = -1;
	idf_val_ = -1;
  }
  Word(std::string name, int dict_id, double idf_val) {
	name_ = name;
	dict_id_ = dict_id;
	idf_val_ = idf_val;
  }
  
  // Get attributes.
  std::string name() const { return name_; }
  int dict_id() const { return dict_id_; }
  double idf_val() const { return idf_val_; }
  int get_byte_size() { return name_.size(); }

  // Set attributes.
  void set_name(const std::string& name) { name_ = name;}
  void set_dict_id(int dict_id) { dict_id_ = dict_id;}
  void set_idf_val(double idf_val) { idf_val_ = idf_val;}
  
  bool Equals(const Word& other_word) const {
	return name_ == other_word.name_;
  }
 private:
  // The word content.
  std::string name_;  
  // Id in the global dictionary. 
  int dict_id_;
  // Idf_value as weight for the particular 
  double idf_val_;
};
