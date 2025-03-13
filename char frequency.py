s=input()
freq = {}
result = []
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char in s:
    if char in freq:
        result.append(f"{char}{freq[char]}")
        del freq[char]
print(" ".join(result))