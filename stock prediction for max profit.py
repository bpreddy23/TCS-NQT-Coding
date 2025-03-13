prices=[list(map(int, input().split()))]
p=len(prices)
profit=[]
if p>1:
    for i in range(p):
        for j in range(i+1,p):
            profit.append(prices[j]-prices[i])
    if max(profit)>0:
        print(max(profit))
    else:
        print(0)
else:
    print(0)
