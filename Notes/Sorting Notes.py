# SORTING NOTES
import random
import time

'''

# Swap values
a = 1
b = 2
print(a, b)
# set a temporary variable to store the value
temp = a
a = b
b = temp
print(a, b)

# the pythonic way
a, b = b, a
print(a, b)

# make a random list of 100 numbers 1 to 99
# use list comprehension
random_list = [random.randrange(1, 100) for x in range(100)]
print(random_list) # we will now sort this list

def selection_sort(my_list):
    for  current_pos in range(len(my_list)):
        minimum_pos = current_pos
        for scan_pos in range(current_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[minimum_pos]:
                minimum_pos = scan_pos
        my_list[current_pos], my_list[minimum_pos] = my_list[minimum_pos], my_list[current_pos]

start_time = time.perf_counter()
selection_sort(random_list)
print("time = ", time.perf_counter() - start_time)
print(random_list)

# Insertion sort
start_time = time.perf_counter()
random_list = [random.randrange(1, 100) for x in range(100)]

print(random_list)

for key_pos in range(1, len(random_list)):
    key_val = random_list[key_pos]
    scan_pos = key_pos - 1  # look to list item on the left
    while scan_pos >= 0 and random_list[scan_pos] > key_val:
        random_list[scan_pos + 1] = random_list[scan_pos]
        scan_pos -= 1
    random_list[scan_pos + 1] = key_val
print("time = ", time.perf_counter() - start_time)
print(random_list)

'''

# Optional Parameters
print("Hello", end=" ")  # end is an optional parameter with a default value of \n
print("World")


def hello(name, time_of_day="Morning"):  # morning is now the default but you can change it
    print("Hello", name, "Good", time_of_day)


hello("Jim", "evening")

# Lambda Function (anonymous function on a single line)
double_me = lambda x: x * 2  # nameless function lambda parameter: return
print(double_me(5))

# Real World Sorting With Python

my_list = [random.randrange(100) for x in range(10)]
print(my_list)
my_2d_list = [[random.randrange(100), random.randrange(100)] for x in range(10)]
name_list = ["ethan", "Benji", "lee", "Nicky", "Jonathan", "Karen", "michelle"]

# sort method- this one changes the list

my_list.sort(reverse=True)  # a parameter that reverses the sort (highest to lowest instead of lowest ot highest)
print(my_list)

name_list.sort(key=lambda x: x.upper())
print(name_list)
name_list.sort(reverse=True, key=lambda x: len(x))
print(name_list)

my_2d_list.sort(key=lambda x: x[1])  # sorts by the second item
#print(my_2d_list)

my_2d_list.sort(key=lambda x: x[0] + x[1]) # you can also sort by (key=sum)
print(my_2d_list)

# The sorted function (returns a new list)
new_list = sorted(my_list, reverse=False)
print(new_list)

new_list = sorted(my_list, key=lambda x: int(str(x)[-1]))
print(new_list)