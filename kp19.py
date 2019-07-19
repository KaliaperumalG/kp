n111,n222=input().split()
n111=int(n111)
n222=int(n222)
for num1 in range(n111,n222):
  sum=0
  temp=num1
  while(temp>0):
     sum=sum+(temp%10)**3
     temp=temp//10
  if(sum==num1):
     print(num1,end=" ")
