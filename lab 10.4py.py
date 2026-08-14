names=[]
for i in range(5):
   name=input("enter a name:")
   names.append(name)
print(names)

for name in names:
   print(name)

for pos,nm in enumerate(names):
    print(pos,nm)

count=0
for name in names:
    if len(name) >5:
        count=count+1
print (count)
