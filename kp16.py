s9,d9=map(int,input().split())
for k in range (s9+1,d9):
    for g in range(2,k):
      if (k%g==0):
        break
    else:
        print(k,end=' ')
