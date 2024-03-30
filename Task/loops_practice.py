
# n = int(input("Enter The Number :"))

# j = 0

# for i in range(1,n):
#     j+=i
# print(j)

# str1 = "Pynative"

# for i in range(1):
#     print(str1[0::2])
#     print(i)


num = input("Enter The Number :")
num1 = num[-1::-1]
print(num)
print(num1)

if(num==num1):
    print("Number Is Palindrome",num1)
else:
    print("number Is not Palindrome ",num1)
