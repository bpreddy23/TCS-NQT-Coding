nums=list(map(int, input().split()))
for i in range(len(nums)):
    result = 0
    for num in nums:
        result ^= num
print(result)
