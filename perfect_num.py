#Check whether a number is perfect or not

def perfect_number(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum += x
    return sum == num
print(perfect_number(6))