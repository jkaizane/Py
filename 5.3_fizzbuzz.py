number = 0

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)