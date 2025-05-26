#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value=''):
    self.value = value 
  @property
  def value(self): 
    return self._value
  
  @value.setter
  def value(self, val):
    if not isinstance(val, str):
        raise ValueError("The value must be a string.")  # No leading space here
    self._value = val


  def is_sentence(self):
     return self.value.endswith('.')

  def is_question(self):
     return self.value.endswith('?')
  def is_exclamation(self):
    return self.value.endswith('!')
  def count_sentences(self):
        # Split on one or more sentence-ending punctuation marks
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out empty or whitespace-only strings
        filtered = [s.strip() for s in sentences if s.strip()]
        return len(filtered)
  


  
  

    
   