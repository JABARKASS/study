array = []

for i in range(7):
    row = []
    for j in range(7):
        if j - i < 0 and i + j < 7 or i == j and j < 4:
            row.append(0)
        else:
            row.append(1)
    array.append(row)

for r in array:
    print(*r)