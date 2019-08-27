import math
a,b=map(int,input().split())
p=a*b
c=int(math.sqrt(p))
d=c*c
if(d==p):
  print("yes")
else:
  print("no")
