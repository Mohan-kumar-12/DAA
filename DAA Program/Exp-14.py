x=int(input("Enter the base: "))
n=int(input("Enter the exponent: "))
result=1
for i in range(n):
    result*=x
print("Answer = ", result)