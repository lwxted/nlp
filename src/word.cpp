#include "word.h"
#include <iostream>

int main() {
  Word test = Word("test", 1, 1);
  std::cout << test.name() << std::endl;
}
