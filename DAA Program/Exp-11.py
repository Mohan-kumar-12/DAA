import heapq
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
heapq.heapify(arr)
sorted_list = []
while arr:
    sorted_list.append(heapq.heappop(arr))
print("Sorted:", sorted_list)