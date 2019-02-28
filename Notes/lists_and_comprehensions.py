#LISTS (29PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.


import random


# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(1,101)]
print(my_list)
# b) Make a list of even numbers from 20 to 40
my_list2 = [x for x in range(20, 41) if x % 2 == 0]
print(my_list2)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list3 = [x ** 2 for x in range(101)]
print(my_list3)

#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]
question = input("Ask A Question: ")
print(answer_list[random.randrange(len(answer_list))])


# PROBLEM 3 (Shuffle - 8pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]

# Then create a function that shuffles the deck, producing a random order. Print the random deck.
deck = []
for value in values:
  for suit in suits:
    deck.append(value + suit) # concatenation
print(deck)

for i in range(len(deck)):
  print(deck[random.randrange(len(deck))])

# Then deal yourself a hand of 5 cards off the top.  Print the hand.  Print the remaining deck.
print("your hand is")
for i in range(5):
  deck_number = random.randrange(len(deck))
  print(deck[deck_number])
  deck.pop(deck_number)
print("The remaining deck consists of: ", deck)



# PROBLEM 4 (Illinois Pick 4 - 10pts)
# Lotteries are known to give awful odds of winning, and incredibly low expected returns on your invevestment.
# You will buy 10000 Illinois Pick 4 tickets in a simulation.
# Make a 2d lists of your picks.  Each number is a random 0 to 9.
lottery_list = []
for i in range (10000):
    draw1 = random.randrange(1, 10)
    draw2 = random.randrange(1, 10)
    draw3 = random.randrange(1, 10)
    draw4 = random.randrange(1, 10)
    lottery_list.append([draw1, draw2, draw3, draw4])
print(lottery_list)

# After you have made a list of 10000 lists (each 4 long), you will draw the official numbers
winning_numbers = []
for i in range(4):
    winning_numbers.append(random.randrange(1,10))

# After drawing the official numbers, you will go back through your list and check to see how many wins you got.
# The numbers must be an exact match in the exact position.
wins = 0
wins = lottery_list.count(winning_numbers)
print("you won", wins, "times")
# Each ticket is $1.  If you win, you get $5000.  Simulate spending $10,000 on Pick 4 tickets, and see your return.
money = wins * 5000
print("You spent $10,000. You won back", money, "dollars.")
