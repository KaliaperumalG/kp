v=list(input())
w=" "
for i in range(len(v)):
    if w in v:
        v.remove(w)
print(len(v))
