"""list=[44,23,789,56,11,8,4004,324]
list.sort()
print(list)
print(list[-1])
print(list[-2])"""


"""list1=[44,23,789,56,11,8,4004,324]
largest = list1[0]

for x in list1:
    if(x>largest):
        largest = x
        print(largest)"""


"""list1=[1,3,2]
list2=[1,5,4]
list3=list1+list2
list3.sort()
print(list3)"""

"""nums=[1,1,0,1,1,1]
count=0
max_count=0
for x in nums:
    if(x == 1):
        count+=1
        if(count > max_count):
            max_count=count
    else:
         count=0
         
print(max_count)"""


"""item=input("enter the name:")
price=int(input("enter the price:"))
quantity=int(input("enter the quantity:"))
total=price*quantity
totalcost=total * 0.05
print(total + totalcost)"""

"""seat1="economy"
seat2="business"
seat3="firstclass"
economy=100
business=200
firstclass=300
count=int(input("enter the number:"))
seat_type=(input("enter cost based on seat type"))
if(seat_type == "economy"):
    print(economy * count)
elif(seat_type == "business"):
    print(business * count)
elif(seat_type == "firstclass"):
    print(firstclass * count)"""


"""order=input("enter the name of food :")
cost=int(input("enter the cost:"))
disc = 0
if(cost>100):
   disc = cost*0.10
else:
    disc = cost * 0.08

print (cost - disc)"""

"""class LinkedList:
   def __init__(self):
      self.head = None
   def insert(self,data):
      if not self.hesd:
         self.head = Node(data)
      else:
         current = self.head
         while current.next:
            current = current.next
         current.next = Node(data)"""

numbers=(1,2,3,4,5,6,7,8,9)
counteven=0
countodd=0
for x in numbers:
   if x %2:
      counteven+=1
   else:
      countodd+=1
print("number of even numbers:",counteven)
print("number of odd numbers:",countodd)
      






