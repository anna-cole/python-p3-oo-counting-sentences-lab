#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith('?'):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else: 
      return False
    
  def count_sentences(self):
    delimiters = ['.', '?', '!']
    sentences = [word for word in self.value.split() if any ([word.endswith(d) for d in delimiters])]
    return len(sentences)


# string = MyString("ana.")
# string.value = "This is a string! It has three sentences. Right?"
#print(string.value)
#string.is_sentence()
#string.count_sentences()
