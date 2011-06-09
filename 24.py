#!/usr/bin/python
from math import factorial
def lex_permutation(digits, target):
  digit_len = len(digits)
  if digit_len == 1:
    return [digits[0]]
  else:
    bucket_size = factorial(digit_len)/digit_len
    digit_to_split_index = target / bucket_size
    digit_split = digits[digit_to_split_index]
    digits.pop(digit_to_split_index)
    return [digit_split] + lex_permutation( digits, target - bucket_size * digit_to_split_index)

if __name__ == '__main__':
  print lex_permutation([0,1,2,3,4,5,6,7,8,9], 1000000)
