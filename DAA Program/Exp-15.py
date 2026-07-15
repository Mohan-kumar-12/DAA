import math

n = int(input("Enter number of points: "))

points = []

print("Enter x y:")
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

min_dist = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        d = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

        if d < min_dist:
            min_dist = d
            p1 = points[i]
            p2 = points[j]

print("Closest Pair:", p1, p2)
print("Distance =", min_dist)