list1=[]
n=int(input("enter array size:"))
for i in range(n):
   num=int(input("Enter the array element %d:"%i))
   list1.append(num)
print(list1)
list1.sort()
Finallist=set(list1)
Finallist1=list(Finallist)
print(Finallist1)
for i in range(len(Finallist)-1):
   Finallist1.append('_')
print(len(Finallist),Finallist1)
