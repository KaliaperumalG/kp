g1=int(input())
df1=[]
for i in range(0,g1):
 ij1=input()
 df1.append(ij1)
ff1=[]
for i in zip(*df1):
 if(i.count(i[0])==len(i)):
  ff1.append(i[0])
 else:
  break
print(''.join(ff1))
