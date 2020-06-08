#tupples are just like lists BUT you cant change their initial values
#they use () instead of [] => this is for lists

#tupple decleration + initialization
mytupple=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")

#this will print "monday"
print(mytupple[0])
#this will print "sunday"
print(mytupple[6])

print("Printing all days of the week:\n")
for i in mytupple:
    print(i)