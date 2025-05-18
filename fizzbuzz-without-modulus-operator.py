count_3 = count_5 = 0

for num in range(1, 100):
    count_3 += 1
    count_5 += 1
    if count_3 == 3 and count_5 == 5:
        print(num, 'fizzbuzz')
        count_3 = count_5 = 0
    elif count_3 == 3:
        print(num, 'fizz')
        count_3 = 0
    elif count_5 == 5:
        print(num, 'buzz')
        count_5 = 0
    else:
        print(num)