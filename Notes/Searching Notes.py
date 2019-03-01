'''
# SEARCHING NOTES (ch15 on programarcadegames)
# We want to be able to take large pieces of data and interpret them
# for instance, villians.txt
'''

# open a file to read
file = open('C:/Users/User/PycharmProjects/Programming2_SP19/Notes/villains.txt', 'r')  # default is r

for line in file:
    print(line.strip())  # strip removes leading and trailing spaces. i. e. /n and /t


file.close()  # make sure to close it

# you can only do the for thing once so if you want to go through it again you need to reopen the file.


# open a file to append

file = open('C:/Users/User/PycharmProjects/Programming2_SP19/Notes/villains.txt', 'a')  # a is for append

file.write("\nLee the Merciless")

file.close()

file = open('C:/Users/User/PycharmProjects/Programming2_SP19/Notes/villains.txt', 'r')
for line in file:
    print(line.strip())
file.close()

# open and write to a file (THIS OVERWRITES YOUR FILE)

file = open('C:/Users/User/PycharmProjects/Programming2_SP19/Notes/oscars.txt', 'w') # creates a new one

file.write("Best Picture - Green Book\n")
file.write("Makeup - Vice\n")

file.close()


# heres an easier way to open a file and read it
with open('C:/Users/User/PycharmProjects/Programming2_SP19/Notes/villains.txt') as f:
    # we opened villains to read and assigned it the name f.
    for line in f:
        print(line.strip(), end="!\n")
        


# To use the data, read it into a list


with open('C:/Users/User/PycharmProjects/Programming2_SP19/Notes/villains.txt') as f:
    villain_list = [x.strip() for x in f]

print(villain_list)

# Linear Search

key = "Claude Avernus" # what we are looking for
i = 0  # index of the loop

while i < len(villain_list) and key != villain_list[i]:
    i = i + 1
if i < len(villain_list):
    print("Got", key, "at position", i)
else:
    print("I couldn't find", key)

# Binary Search

# first lets sort our list

villain_list.sort()

key = "Renard the Torturer"
lower_bound = 0
upper_bound = len(villain_list) - 1
found = False

# loop until we find it
loops = 0

while lower_bound <= upper_bound and not found:
    loops += 1
    middle_position = (upper_bound + lower_bound) // 2
    if villain_list[middle_position] < key:
        lower_bound = middle_position + 1
    elif villain_list[middle_position] > key:
        upper_bound = middle_position - 1
    else:
        found = True
if found:
    print("Found", key, "at position", middle_position, "after", loops, "loops")
else:
    print("Could not find", key, "after", loops, "loops")

# Read in Alice
import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


villains = open('villains.txt', 'r')

for villain in villains:
    words = split_line(villain.strip())
    for word in words:
        print(word)