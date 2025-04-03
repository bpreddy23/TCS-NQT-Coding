arr=list(map(int,input().split()))
n = int(input())
if n in arr:
    ar=arr.index(n)
    print(ar)
else:
    print("no")