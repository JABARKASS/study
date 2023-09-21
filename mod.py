import math


def expression(x):
  if x == 0:
    print("!!! ДІЛЕННЯ НА 0 !!!")
    z = 0
  else:
    z = math.sqrt(2) / 2 * (math.sin(1 / x)) + 1
  return z


def dilniki(n):
  if n <= 1:
    return False
  sum = 1
  for i in range(2, n):
    if n % i == 0:
      sum += i
  if n == sum:
    return True
  else:
    return False
