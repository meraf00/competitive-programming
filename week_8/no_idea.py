# Enter your code here. Read input from STDIN. Print output to STDOUT

size_a, size_b = list(map(int, input().split(" ")))

array = map(int, input().split(" "))

a = set(map(int, input().split(" ")))
b = set(map(int, input().split(" ")))

happiness = 0
for element in array:
    if element in a:
        happiness += 1
    elif element in b:
        happiness -= 1

print(happiness)
        