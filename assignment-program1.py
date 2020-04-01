a = [('a',1),('a',3),('a',5),('b',2),('b',6),('c',1),('c',2),('c',3),('c',4),('c',5),('d',4),('d',5),('d',6),('d',7),('e',1),('e',3),('e',5),('e',6),]
low = []
for i,j in a :
    if i not in low :
        low.append(i)
print(low)
dic = {}
lit = []
s = set()
b = ''
for i in low :
    for j,k in a :
        if  i == j :
            b = b + str(k)
        else :
            continue
    dic.update({i:set(b)})
    b = ''
print(dic)
chk = 0
chk2 = 0
q = ''
kk = []
t = ()
for i in dic.values() :
    for j in dic.values() :
        if i == j :
            continue
        else :
            if len(i) > len(j) :
                for m in i :
                    if m in j :
                        chk = chk +1
                if chk2 < chk :
                    chk2 = chk
                    h = i
                    o = j
                chk = 0
            else :
                for n in j  :
                    if n in i :
                        chk = chk +1
                if chk2 < chk :
                    chk2 = chk
                    h = i
                    o = j
                chk = 0
for ke,val in dic.items() :
    if h == val :
        t += (ke,)
    if o == val :
        t += (ke,)
kk.append(t)
print(kk)