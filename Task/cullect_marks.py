
marks ={}
phy = int(input("Enter Physics Marks :"))
Chem = int(input("Enter Chemistry Marks "))
Bio = int(input("Enter Biology Marks :"))

marks.update({ "phy" : phy})
marks.update({ "Chem" : Chem})
marks.update({ "Bio" : Bio})

print(marks)