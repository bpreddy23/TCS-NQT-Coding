nums = list(map(int, input().split()))
if not nums:
    print(nums)
    exit()
j = 0
for i in range(1, len(nums)):
    if nums[i] != nums[j]:
        j += 1
        nums[j] = nums[i]
nums = nums[:j + 1]
print(nums)
