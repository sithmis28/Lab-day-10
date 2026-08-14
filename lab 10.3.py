numbers=[]
for i in range(5):
   num=int(input("enter your number:"))
   numbers.append(num)
print("numbers",numbers)
tot=sum(numbers)
avg=tot/len(numbers)
print("total is",tot)
print("average is",avg)
