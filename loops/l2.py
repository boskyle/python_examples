# loop through a dictionary

age = {"Bos":21,"John":20,"Martin": 24,"Andrea": 23}

for i in age:
    print(i)

print()

# first iteration will assign string "Bos" to variable 'i' becoming => "Bos" => age["Bos"] 
for i in age:
    print("Name = %s\tAge = %d" %(i,age[i]))
