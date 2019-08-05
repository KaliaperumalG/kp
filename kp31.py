n,a,d=map(int,input().split())
s1=a
for i in range(1,n):
  s1=s1+((d*i)+a)
print(s1)
