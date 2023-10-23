data=[]
n=int(input('Enter no of elements:'))
for i in range(0,n):
    x=int(input())
    data.append(x)
l=data[0]
s=data[0]
for num in data:
    if num>l:
        l=num
    elif num<s:
        s=num
print('Max=',l)
print('Min=',s)
