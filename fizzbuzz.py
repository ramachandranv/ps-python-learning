for num in range(100):
    if (num % 3 == 0) and (num % 5 == 0):
        print(num, 'fizzbuzz')
    elif (num % 3 == 0):
        print(num, 'fizz')
    elif (num % 5 == 0):
        print(num, 'buzz')
    else:
        print(num)