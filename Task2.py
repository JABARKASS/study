import math

from mod import expression
from mod import dilniki

x = float(input("Введіть значення х : "))
print("z = ", expression(x))

n = int(input("Введіть число n: "))
if dilniki(n) == True:
  print(f"{n} не є недостатнім числом.")
else:
  print(f"{n} є недостатнім числом.")
