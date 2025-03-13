l=list(map(int, input().split()))
i=0
su=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] == l[j]:
            su+=1
print(su)