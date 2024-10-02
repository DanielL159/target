def is_fibonacci(num):
    fibonacci = [0,1]

    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return num in fibonacci


while True:
    try:
        number = int(input('Please give me a number: '))

        if number < 0:
            print('Please enter a positive number.')
        else:
            break
    except ValueError:
        print('Invalid input. Please enter a valid Integer')

if is_fibonacci(number):
    print("It's a Fibonacci number")
else:
     print("It's not a Fibonacci number")
