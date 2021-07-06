lst = []
list2 = int(input("Enter the Number: "))
for i in range(0,list2):
    num1 = int(input())
    lst.append(num1)
print("List:", lst)

print("Smallest Number: ",min(lst))
print("Largest Number: ", max(lst))