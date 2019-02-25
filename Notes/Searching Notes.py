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