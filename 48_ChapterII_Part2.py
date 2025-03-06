
def average(numlist):
    avg = sum(numlist) / len(numlist)
    return avg
numberlist = input("Enter list of numbers: ").split()
print(average(list(map(int, numberlist))))
