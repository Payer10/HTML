price,discount = map(int,input().split())
ans = (discount*price)/100
a = price - ans
print('%.2f'%a)