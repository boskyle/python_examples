#prime checker

def checkIfPrime (numToCheck):
    for x in range(2, numToCheck):
        # if number is divisible by 0 then not prime else => prime
        if (numToCheck%x == 0): 
            return False
        return True

answer = checkIfPrime(6)
print(answer)