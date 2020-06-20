

# a star in front of a function parameter means that you could pass 1 more or more argument to it
def meSum(*nums):
    sum = 0
    for i in nums:
        sum += i
    print(sum)


meSum(5,5,2)

