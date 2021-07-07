lst = []
list1 = int(input("Number you wanted to enter: "))

for i in range(0,list1):
    ele = int(input())
    lst.append(ele)
print("List: ",lst)
lst = [x for x in lst if x%2!=0]

print("List without even number: ",lst)

