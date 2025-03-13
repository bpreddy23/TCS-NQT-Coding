n=int(input())
k=[]
for i in range(1,n):
    if n%i==0:
        k.append(i)
if sum(k)==n:
    print(True)
else:
    print(False)