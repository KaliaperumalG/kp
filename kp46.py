#k
x11=input()
y12=0
for i in range(len(x11)):
    if (x11[i].isalpha() or x11[i].isnumeric() or x11[i]==" "):
      continue
    y12=y12+1
else:
    print(y12)
