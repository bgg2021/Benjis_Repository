# Alice in wonderland spellchecker

import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_list = []

file = open('C:\Users\User\PycharmProjects\Programming2_SP19\Labs And Problem Sets\dictionary', 'r')
for line in file:
    line = line.strip()
    dictionary_list.append(line)
print(dictionary_list)