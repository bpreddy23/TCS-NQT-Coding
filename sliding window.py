arr=list(map(int, input().split()))
k=int(input())
res=[]
for i in range(len(arr)-k+1):
    l=[]
    for j in range(i,i+k):
        l.append(arr[j])
    ma=max(l)
    res.append(ma)
print(res)