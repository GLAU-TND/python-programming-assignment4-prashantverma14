l = ['dog','deer','deal']
s = 'de'
l1 = []
for i in range(len(l)) :
    if l[i][0]+l[i][1] == s :
        l1.append(l[i])
print(l1)
