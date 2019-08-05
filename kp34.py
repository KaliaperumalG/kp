x=int(input())
a=list(map(int,input().split()[:x]))
a.sort()
for i in a:
  print(i,end="  ")
