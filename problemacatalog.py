#lista sortata
import string
b=[]
with open('input.txt','r') as f:
    lista=f.readlines()
print(lista)

k=0
for h in range(len(lista)):
    k+=1
for x in lista:
    if x!=lista[k-1]:
        x = x[:-1]
        b.append(x)
    else:
        x=x
        b.append(x)
y=sorted(b)
with open('catalog.txt','w') as f:
    for e in y:
        f.write(e)
        f.write("\n")

