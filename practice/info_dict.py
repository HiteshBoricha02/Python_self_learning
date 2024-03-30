

details = {
    
    "Name" : ["Hitesh","fenil","Mihir","Kishan"],
    
    "Roll_no" :(1,2,3,4),
    
     "percentage" : [89,90,29,28]
     
}
 


# print(details.keys())

# print(details.values())

# print(details.items())
# print(details.get("Name"))

# print(list(details.values()))

# pair = list(details.items())

# print(pair[2])

update_detail ={"Name":["vijay","Piyush","Rajesh","Jaynesh"],
                
                "Roll_no":(5,6,7,8),
                
                "percentage":[95,85,68,98]
                }

details.update(update_detail)

print(details)