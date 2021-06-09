"""
提取文本中的單詞，並計數
"""

__author__ = 'wbs'
__version__ = '0.1'
 
from os.path import abspath
import fileinput
import re

file = abspath(input("Please entry file abspath: "))

regex = re.compile("[a-z]*")

words = {}

with fileinput.input(file) as input:
    for line in input:
        temp = regex.findall(line.lower())
        for word in temp:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        
print(sorted(words.items(), key = lambda kv:(kv[1], kv[0])))
