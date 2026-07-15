n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter key to search: "))
found = -1
for i in range(n):
    if arr[i] == key:
        found = i
        break
if found != -1:
    print("Key found at index", found)
else:
    print("Key not found")