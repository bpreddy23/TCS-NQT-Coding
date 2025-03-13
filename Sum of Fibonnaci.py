n = int(input())
a = 0
b = 0
sumf = 1

if n <= 0:
    sumf = 0
else:
    curr = 1
    for i in range(1, n):
        a = b
        b = curr
        curr = a + b
        sumf += curr

print("The sum of Fibonacci numbers is:", sumf)
