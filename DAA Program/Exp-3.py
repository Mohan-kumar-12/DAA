def recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive(n - 1)
n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Iterative:", fact)
print("Recursive:", recursive(n))