string1=input()
string2=input()
print(''.join(char for char in string1 if char not in string2))