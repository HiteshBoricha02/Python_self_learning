
Name = input("Enter Your Name :")
ROll_No = int(input("Enter Your ROll NO :\t"))
HTML = int(input("Enter HTML Marks :\t"))
CSS = int(input("Enter CSS Marks :\t"))
JAVA = int(input("Enter JAVA Marks :\t"))
PYTHON = int(input("Enter PYTHON Marks :\t"))
BOOTSTRAP = int(input("Enter BOOTSTRAP Marks :\t"))

TOTAL = HTML+CSS+JAVA+PYTHON+BOOTSTRAP
print("TOTAL Marks Is :\t",TOTAL)
Percentage = (TOTAL/500)*100
print("Percentage Is :\t",Percentage)


if(HTML<=32 or CSS<=32 or JAVA<=32 or PYTHON<=32 or BOOTSTRAP <=32 ):
    RESULT = "Fail"
    print(RESULT)
    
elif(Percentage >= 90):
    Grade = "A"
    print( "Your Grade :",Grade)
    
elif(Percentage >= 80):
    Grade = "B"
    print("Your Grade is :",Grade)
elif(Percentage >= 70):
    Grade = "C"
    
elif(Percentage >=60):
    Grade = "D"
    print("Your Grade is :",Grade)
elif(Percentage >=50):
    Grade = "E"
    print("Your Grade is :",Grade)
else:
    Grade = "F"
    # print("Your Grade is :",Grade)
    
    
    print(" Grade is :",Grade)
    