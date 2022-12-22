# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

import math

N = int(input("Задайте число: "))

for i in range(2, int(math.sqrt(N)) + 1): 
    while (N % i == 0): 
        print(i)
        N //= i 

if (N != 1): 
    print (N)




