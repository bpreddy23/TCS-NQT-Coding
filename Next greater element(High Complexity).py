nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
l = []

for i in range(len(nums1)):
    found = False
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            for r in range(j + 1, len(nums2)):
                if nums2[r] > nums2[j]:
                    l.append(nums2[r])
                    found = True
                    break
            if not found:
                l.append(-1)
            break

print(l)
