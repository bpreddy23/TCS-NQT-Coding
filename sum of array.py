arr=[]
n=int(input())
for i in range(n):
    v=int(input())
    arr.append(v)
su=0
for v in arr:
    su+=v
print(su)