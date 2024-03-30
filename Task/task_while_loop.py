
# count = 0
# while count<=100 :
#     print(count)
#     count+=1

# count = 100

# while count>=0 :
#     print(count)
#     count-=1

# cont = 1
# while cont <=10:
#     print(cont*5)
#     cont+=1
    
    
# number = [1,4,9,16,25,36,49,64,81,100]
# a = 0

# while a<(len(number)) :
#     print(number[a])
#     a+=1
    
    
nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter Value"))
i = 0


while i < len(nums):
    if(nums[i]==x):     
         print(x,"is Found At IDX:",i)
    i+=1
    break
    
else:
     print(x,"Your Value is not found in tuple IDX",i)
     #  break
        

