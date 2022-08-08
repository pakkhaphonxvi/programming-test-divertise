def FizzBuzz():
    i = 1
    while(i<=100):
        if((i%3 == 0)and(i%5 == 0)):
            print("FizzBuzz", end = ' ')
        elif(i%3 == 0):
            print("Fizz", end = ' ')
        elif(i%5 == 0):
            print("Buzz", end = ' ')
        else:
            print(i, end = ' ')
        i = i+1

def FibonacciSequence(x):
    y = 0
    temp = 0
    a = 0
    b = 1
    while(y<x):
        print(temp)
        temp = a + b
        b = a
        a = temp
        y = y + 1

# FizzBuzz()
# FibonacciSequence(10)