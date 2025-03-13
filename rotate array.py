nums=list(map(int, input().split()))
k=int(input())
k=k%len(nums)
l=[]
for i in range(len(nums)-k, len(nums)):
    l.append(nums[i])
for i in range(len(nums)-k):
    l.append(nums[i])
for i in range(len(nums)):
    nums[i]=l[i]
print(nums)