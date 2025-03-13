nums=list(map(int, input().split()))
k=int(input())
i=0
tot=0
if len(nums)!=1:
    for j in range(1,len(nums)):
        a=k-nums[i]
        i+=1
        if a in nums:
            tot+=1
print(tot)