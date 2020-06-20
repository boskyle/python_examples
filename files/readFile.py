f=open("file1.txt",'r')


# everytime readline() function is called a \n is appended to the end of the first string
firstline=f.readline()
secondline=f.readline()
print(firstline)
# to not have the \n (line break), print(firstline,end = ")
print(secondline)
f.close()


