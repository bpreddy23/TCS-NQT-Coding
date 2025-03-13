import math
class Solution:
	def numberOfPaths(self, m, n):
		return math.factorial(m+n-2)//(math.factorial(m-1)*math.factorial(n-1))
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        m, n = input().split()
        m = int(m)
        n = int(n)
        ob = Solution()
        print(ob.numberOfPaths(m, n))
        print("~")