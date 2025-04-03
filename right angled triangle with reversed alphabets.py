n = int(input())
for i in range(0,n+1):
    ch=65+n-i
    for j in range(i+1):
        print(chr(ch+j),end='')
    print()