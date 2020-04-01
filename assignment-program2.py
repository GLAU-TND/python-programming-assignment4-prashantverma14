def final_dic(i,j) :
    dic1 = {}
    for k,l in j.items() :
        if type(l)!=dict:
            dic1[i+'.'+k] = l
     while(type(l)==dict):
         for m,n in l.items():
             dic1[i+'.'+k+'.'+m]=n
        break
    return(dic1)
dic = {'key':3,'foo':{'a':5,'bar':{'baz':0}}}
fin = dict()
for i,j in dic.items() :
    if type(j) is dict :
        fin.update(final_dic(i,j))
    else :
        fin[i] = j

print(fin)