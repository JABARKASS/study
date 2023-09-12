print("Task 1 : ")
a = int(input("Enter a = "))
while (a < 1 or a > 100):
  a = int(input("Enter а again = "))
b = int(input("Enter b = "))
while (b < 1 or b > 100):
  b = int(input("Enter b again = "))

if a > b:
  r = (b * a + 1)
elif a == b:
  r = 3425
else:
  r = (2 * a - 5) / b

print("RESULT = ", r)

print("")
print("Task 2 : ")
for i in range(1, 10):
  print(2**i)

print("")
print("Task 3 : ")
n = int(input("Enter N layers  = "))
m = n
for j in range(0, n):
  j = n
  print("#" * n)
  n = n - 1
j = 1
for j in range(1, m+1):
  print("#" * j)
  j = j + 1
