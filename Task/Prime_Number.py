
start = int(input("Enter THe starting Number :"))
end = int(input("Enter The ending Number :"))

print("Prime numbers between", start, "and", end, "are:")

for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i,"Is prime Number ")
            
            
