
list = [34,55,67,88,98,67]


print("Print normal List :",list)

list.append(100) # Add one element at the end
print("Add Append Method :",list)

list.sort()    # Sort in ascending order
print("Ascending Order :",list)

list.sort(reverse = True)   # sort in descending order
print("print descending order :",list)

list.reverse()  # list in revers order
print("Print list in Revers order :",list)


list.insert(1,101) #insert Element in idx
print("Insert Element at idx :",list)


list.remove(100)  #Remove element you select
print("Remove 100 in list :",list)


list.pop(0)   #Remove Index of list
print("Remove Index :",list)

