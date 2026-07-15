n=int(input("Enter the number of elements: "))
arr=list(map(int,input("Enter the elements: ").split()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            count+=1
print("Counting Inversions = ", count)