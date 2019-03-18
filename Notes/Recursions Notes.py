# RECURSIONS- function iNcEptIoN


def f():
    print("f")
    g()


def g():
    print("g")

# functions can call themselves (this causes a recursion error) or other functions
f()

# controlling recursion with depth
def controlled(depth, max_depth):
    print("Recursion depth:", depth)
    if depth < max_depth:
        controlled(depth + 1, max_depth)
    print("Recursion depth", depth, "has closed.")


# factorial
def factorial(number):
    total = 1
    for i in range(1, number + 1):
        total = total * i
    return total
print(factorial(10))

def recursive_factorial(n):
    if n > 1:
        return n * recursive_factorial(n - 1)
    else:
        return n
print(recursive_factorial(10))