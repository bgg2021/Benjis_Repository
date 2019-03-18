# EXCEPTIONS AND RECURSIONS NOTES

# an exception is... well... the easiest way is to just show it.
# if the try works, great. If it doesn't, it does the 'except'.



try:
    val = int(input("Enter a number: "))
except:
    print("You entered an invalid number") # so this is basically if the user doesn't meet the try condition



#  Error types:

# ValueError
try:
    pass
    #val = float(input("Enter a number: "))
except ValueError:
    print("You Entered an invalid number")

# ZeroDivisonError
try:
    y = 5 / 0
except ZeroDivisionError:
    print("Zero Division Error")

# I/O Error  - FileNotFoundError
try:
    my_file = open("nonexistent_file.txt")
    for line in my_file:
        print(line)
except FileNotFoundError:
    print("You can't open that file, because it doesn't exist.")

# Identifying Errors
try:
    y = 1 / 0
    int("A")
except Exception as e:
    print("So the error with this one had to do with", e)

# Multiple Error Types
try:
    int("A")
except ValueError:
    print("there's a value error")
except ZeroDivisionError:
    print("there's a zero division error")
finally:
    print("This code always runs")
    


# make an MPG calculator (miles per gallon)

done = False

while not done:
    try:
        miles = float(input("Miles: "))
        gal = float(input("Gallons: "))
        done = True
    except ValueError:
        print("enter valid numbers")

try:
    mpg = miles / gal
    print("MPG: ", mpg)
except ZeroDivisionError:
    print("You have infinite MPG")

# Ok, time for part 2: Recursions