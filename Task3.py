import string

ryadok = input("Введіть символи : ")

print("Рядок , поч. з 2-го симв. спочатку та до 2-го симв. з кінця : ",
      ryadok[1:-1])

word = input("Введіть слово кирилицею : ")

if any(char in "iao" for char in word):
  print("У слові є підміна на латинські a , або o , або i .")
else:
  print("У слові немає підміни на латинскьі букви .")

sentece = input("Введіть речення : ")
asciisentence = ""

for char in sentece:
  if char.isalpha():
    ascii_code = ord(char)
    asciisentence += str(ascii_code)
  else:
    asciisentence += char

print("Дане речення у ASCII системі виглядає так : ", asciisentence)
