

# def add(a,b):
#     return a + b


# sum = add(3,5)
# print(sum)


print("----------Chose The method-----------")
print("---------------Addition--------------")
print("---------------Subtraction-----------")
print("---------------Multiplication-----------")
print("---------------Division-----------------")

A = int(input("Enter The Value Of A :"))
B = int(input("Enter The Value of B :"))

choice = input("Enter Your Choice :")

if(choice == "Addition"):
    def ADD(A,B):
      return A + B
    
    Add = ADD(A,B)
    print("Your Choice is Addition")
    print(f"Addition Of {A} And {B} Is => {Add}")
    
elif(choice == "Subtraction"):
    def ADD(A,B):
      return A - B
    
    Add = ADD(A,B)
    print("Your Choice is Subtraction")
    print(f"Subtraction Of {A} And {B} Is => {Add}")

elif(choice == "Multiplication"):
    def ADD(A,B):
      return A * B
    
    Add = ADD(A,B)
    print("Your Choice is Multiplication")
    print(f"Multiplication Of {A} And {B} Is => {Add}")
    
elif(choice == "Division"):
    def ADD(A,B):
      return A / B
    
    Add = ADD(A,B)
    print("Your Choice is Division")
    print(f"Division Of {A} And {B} Is => {Add}")
else:
    print("Please Enter The valid Choice :")