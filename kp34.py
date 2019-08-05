bb2=int(input())
b=list(map(int,input().split()[:bb2]))
b.sort()
for i in b:
  print(i,end=" ")
