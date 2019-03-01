import re

# This function takes in a line of text and returns
# a list of words in the line.
from typing import List


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
dictionary = open('dictionary', 'r')
for line in dictionary:
    word = line.strip()
    dictionary_list = [x.strip() for x in dictionary]
    dictionary_len = [len(x) for x in dictionary_list]
print(dictionary_list[dictionary_len.index(max(dictionary_len))])

#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
alice_list = []
tally = 0
alice_in_wonderland = open('alice_fullbook', 'r')
for line in alice_in_wonderland:
    words = split_line(line.strip())
    for word in words:
        alice_list.append(word)
        tally = tally + len(word)
print("Alice in Wonderland has", len(alice_list), "words in it")
print("The average word length is", tally / len(alice_list))


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"
seven_letter_list = []
alice_in_wonderland = open('alice_fullbook', 'r')
for line in alice_in_wonderland:
    words = split_line(line.strip())
    for word in words:
        if len(word) == 7:
            seven_letter_list.append(word)
count_list = [seven_letter_list.count(x) for x in seven_letter_list]
position = (count_list.index(max(count_list)))
print("The most frequently occurring seven letter word is '", seven_letter_list[position], "'")

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.