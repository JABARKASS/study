n = int(input("Enter N elements in array = "))
array1 = [0]*n

for k in range (n):
  array1[k] = int(input("Enter element of array : "))

reverse = array1[::-1]
print(reverse)

array2 = []

for i in range(7):
    row = []
    for j in range(7):
        if j - i < 0 and i + j < 7 or i == j and j < 4:
            row.append(0)
        else:
            row.append(1)
    array2.append(row)

for r in array2:
    print(*r)
