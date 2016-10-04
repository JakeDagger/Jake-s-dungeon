def convertToBinary(n):

if n > 1:
    convertToBinary(n//2)
print(n % 2,end = '')

decimal = int(input("give me a number: "))

convertToBinary(decimal)

