x=list(input())
y=" "
for i in range(len(x)):
    if y in x:
        x.remove(y)
print(len(x))
