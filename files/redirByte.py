inputFile = open("file1.txt",'r')
outputFile = open ("file2.txt",'w')

# specify to read only 10 bytes from file1.txt == 10 characters
# store it to buffer "msg"
msg = inputFile.read(10)

# each char is 1 byte long, the write function below proves this
while len(msg):
    # outputFile.write(msg)
    outputFile.write(msg+"\n")
    # keeps re-assigning the input file value to msg until reach end of file
    msg = inputFile.read(10) 


inputFile.close()
outputFile.close()

