

# list_1 =[1,4,9,16,25,36,49,64,81,100]

# for num in list_1:
#     print(num)

tup_1 =(1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter The value :"))
idx = 0
for el in tup_1:
    if(el == x):
        print(x,"is Found IDX",idx)
        break
    else:
        print("Value is not Found In Tuple")
        # break
    idx+=1
        