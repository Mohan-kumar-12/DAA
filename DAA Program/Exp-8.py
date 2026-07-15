def hanoi(n, source, helper, destination):
    if n == 1:
        print(source, "->", destination)
        return
    hanoi(n - 1, source, destination, helper)
    print(source, "->", destination)
    hanoi(n - 1, helper, source, destination)
n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'B', 'C')