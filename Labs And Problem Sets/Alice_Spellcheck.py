# Alice in wonderland spellchecker
#Benji Gourdji

import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_list = []

file = open('dictionary', 'r')
for line in file:
    line = line.strip()
    dictionary_list.append(line)
def linear_search(key, dictionary):
    i = 0
    while i < len(dictionary) and dictionary[i] != key:
        i += 1
    if i < len(dictionary):
        return(False)
        #print("found", key, "at pos", i)
    else:
        return(True)

def binary_search(key, dictionary):
    lower_bound = 0
    upper_bound = len(dictionary) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2
        if dictionary[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif dictionary[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
       return(False)
    else:
        return(True)


print("--- Linear Search ---")
line_number = 0
alice_lines = []
alice_ch1 = open('alice_ch1', 'r')
for line in alice_ch1:
    words = split_line(line.strip())
    alice_lines.append(words)
for i in range (len(alice_lines)):
    for word in alice_lines[i]:
        found = linear_search(word.upper(), dictionary_list)
        if found:
            print("Line", i, "possible misspelled word: ", word)



print("--- Binary Search ---")
alice_lines2 = []
alice_ch1 = open('alice_ch1', 'r')
for line in alice_ch1:
    words = split_line(line.strip())
    alice_lines2.append(words)
for i in range (len(alice_lines2)):
    for word in alice_lines2[i]:
        found = binary_search(word.upper(), dictionary_list)
        if found:
            print("Line", i, "possible misspelled word: ", word)