n = int(input())
l = [int(digit) for digit in str(n)]
su = sum(digit ** 3 for digit in l)
if su == n:
    print("True")
else:
    print("False")
