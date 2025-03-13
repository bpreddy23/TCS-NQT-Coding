nums=list(map(int, input().split()))
target=int(input())
r = []
for i in range(len(nums)):
    t = target - nums[i]
    if t in nums and nums.index(t) != i:
        r.append(i)
        r.append(nums.index(t))
        break
print(r)