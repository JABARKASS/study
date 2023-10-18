def realtointeger(float_list):
  integer_list = [int(round(num)) for num in float_list]
  return integer_list

def shortestword(words):
  shortest_word = min(words, key=len)
  return shortest_word

import random

def sameelements():
  set1 = set(random.sample(range(1, 100), 19))
  set2 = set(random.sample(range(1, 100), 19))
  
  common_elements = set1.intersection(set2)
  return common_elements

float_list = [0.6, 2.5000001, 4.8, 1.9999999]
int_list = realtointeger(float_list)
print(int_list)

words = ["Людина", "Інформаційні", "Технології", "Мати"]
shortest = shortestword(words)
print(shortest)

same_elements = sameelements()
print(same_elements)