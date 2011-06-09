#!/usr/bin/python
import sys
# How many letters would be needed to write all the numbers in words from 1 to 1000
digits = (
'',
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine'
)
teens = (
'ten',
'eleven',
'twelve',
'thirteen',
'fourteen',
'fifteen',
'sixteen',
'seventeen',
'eighteen',
'nineteen',
)
tens = ('','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
def num_letters(num):
  ret = ''
  if num == 1000:
    ret += 'one thousand'
  elif num < 1000:
    if num >= 100:
      ret += digits[num/100]+'hundred'
      if 0 < num % 100 < 10:
        ret += 'and' + digits[num%100]
      elif 20 > num % 100 >= 10:
        ret += 'and' + teens[num%10]
      elif num % 100 >= 20:
        ret += 'and' + tens[num%100/10] + digits[num%10]
    elif num < 100:
      if num < 10:
        ret += digits[num]
      elif num < 20:
        ret += teens[num%10]
      else:
        ret += tens[num/10]+digits[num%10]
  print ret,
  return len(ret.replace(' ',''))


if __name__ == '__main__':
  tot = 0
  for i in xrange(1,1001):
    print i,
    num = num_letters(i)
    print num
    tot += num
  print tot
