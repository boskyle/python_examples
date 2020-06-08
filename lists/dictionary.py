#data pairs => dictionary, unique key = value
# can be done in two ways {key : value} OR using dict (key = value)

mydic={"Boswell":21,"John":14,"Kayla": 19,"Lowe":17}
#note that the key doesnt have to be a string => it can be value key to value
mydic2={22:21,54:53}
print(mydic)
#this will give the value => 21
print(mydic["Boswell"])
#this will give the value => 17
print(mydic["Lowe"])

#this will display the value => 53
print(mydic2[54])
 
