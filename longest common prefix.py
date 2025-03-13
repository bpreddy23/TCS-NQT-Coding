strs=input().split()
strs.sort()
first, last = strs[0], strs[-1]
common_prefix = []
for i in range(min(len(first), len(last))):
    if first[i] == last[i]:
        common_prefix.append(first[i])
    else:
        break
print("".join(common_prefix))