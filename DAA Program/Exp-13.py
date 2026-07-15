n=int(input("Enter the number of elements: "))
arr=list(map(int,input("Enter the elements: ").split()))
current=arr[0]
maximum=arr[0]
for i in range(1,n):
    current=max(arr[i],current+arr[i])
    maximum=max(maximum,current)
print("Maximum Sum= ",maximum)