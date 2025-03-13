num=int(input())
if num == 0:
    print(num)
hex_chars = "0123456789abcdef"
result = []
num &= 0xFFFFFFFF
while num > 0:
    result.append(hex_chars[num % 16])
    num //= 16
print("".join(result[::-1]))