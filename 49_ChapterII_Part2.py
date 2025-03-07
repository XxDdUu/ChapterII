import math
def primeCheck(number):
    if number > 1:
        for i in range(2, int(math.sqrt(number))):
            if number % i == 0:
                return False
                break
            else:
                return True
    else:
        return False
print(primeCheck(11))