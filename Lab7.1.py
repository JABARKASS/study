# ФУНКЦІЇ ПРОГРАМИ

# БАЗОВИЙ РОЗКЛАД ПОЇЗДІВ
rozklad_poizdiv = {
    1: {
        "призначення": "Київ - Харків", "прибуття": (8, 15), "відправлення": (6, 30)
    },
    2: {
        "призначення": "Львів - Одеса", "прибуття": (13, 45), "відправлення": (23, 0)
    },
    3: {
        "призначення": "Харків - Дніпро", "прибуття": (11, 30), "відправлення": (8, 45)
    },
    4: {
        "призначення": "Одеса - Львів", "прибуття": (13, 0), "відправлення": (0, 15)
    },
    5: {
        "призначення": "Суми - Київ", "прибуття": (14, 45), "відправлення": (10, 0)
    },
    6: {
        "призначення": "Київ - Львів", "прибуття": (23, 55), "відправлення": (18, 45)
    },
    7: {
        "призначення": "Львів - Київ", "прибуття": (10, 5), "відправлення": (2, 15)
    },
    8: {
        "призначення": "Харків - Одеса", "прибуття": (6, 45), "відправлення": (22, 0)
    },
    9: {
        "призначення": "Одеса - Харків", "прибуття": (15, 0), "відправлення": (7, 15)
    },
    10: {
        "призначення": "Дніпро - Львів", "прибуття": (13, 30), "відправлення": (4, 45)
    }
}


# ВИВЕДЕННЯ РОЗКЛАДУ
def vivedennya_rozkladu(rozklad):
  for train_number, train_info in rozklad.items():
    print(f"Номер поїзда: {train_number}")
    print(f"Призначення: {train_info['призначення']}")
    print(
        f"Відправлення: {train_info['відправлення'][0]:02d}:{train_info['відправлення'][1]:02d}"
    )
    print(
        f"Прибуття: {train_info['прибуття'][0]:02d}:{train_info['прибуття'][1]:02d}"
    )
    print()


# ДОДАВАННЯ ПОЗИЦІЇ ДО СЛОВНИКА
def dodavannya_rozkladu(rozklad, number, destination, arrival, departure):
  if number in rozklad:
    print("Поїзд з таким номером вже існує.")
  else:
    rozklad[number] = {
        "призначення": destination,
        "прибуття": arrival,
        "відправлення": departure
    }
    print("Поїзд додано до розкладу.")


# ВИДАЛЕННЯ ПОЗИЦІЇ ЗІ СЛОВНИКА
def vidalennya_rozkladu(rozklad, number):
  if number in rozklad:
    del rozklad[number]
    print("Поїзд видалено з розкладу.")
  else:
    print("Поїзд з таким номером не існує.")


# ВИЗНАЧ. ПРИСУТНОСТІ ПОЇЗДА У ЗАДАНОМУ ЧАСІ
def poizdi_na_stantsii(rozklad, hour, minute):
  poizdi = []
  for train_number, train_info in rozklad.items():
    if (train_info["відправлення"][0] < hour or (train_info["відправлення"][0] == hour and train_info["відправлення"][1] <= minute)) and \
       (train_info["прибуття"][0] > hour or (train_info["прибуття"][0] == hour and train_info["прибуття"][1] >= minute)):
      poizdi.append((train_number, train_info["призначення"]))
  return poizdi


# ПРОГРАМА

while True:
  print("Оберіть опцію:")
  print("1 - Виведення розкладу поїздів")
  print("2 - Додавання нового поїзда до розкладу")
  print("3 - Видалення поїзда з розкладу")
  print("4 - Визначення поїздів на станції в заданий момент часу")
  print("5 - Вихід")

  option = input("Ваш вибір: ")

  if option == "1":
    vivedennya_rozkladu(rozklad_poizdiv)
  elif option == "2":
    number = int(input("Введіть номер поїзда: "))
    destination = str(input("Введіть призначення: "))
    arrival = tuple(
        map(
            int,
            input("Введіть час прибуття (години та хвилини, через пробіл): ").
            split()))
    departure = tuple(
        map(
            int,
            input(
                "Введіть час відправлення (години та хвилини, через пробіл): "
            ).split()))
    dodavannya_rozkladu(rozklad_poizdiv, number, destination, arrival,
                        departure)
  elif option == "3":
    number = int(input("Введіть номер поїзда для видалення: "))
    vidalennya_rozkladu(rozklad_poizdiv, number)
  elif option == "4":
    hour = int(input("Введіть годину: "))
    minute = int(input("Введіть хвилини: "))
    poizdi = poizdi_na_stantsii(rozklad_poizdiv, hour, minute)
    if poizdi:
      print("Поїзди, які знаходяться на станції у цей час:")
      for train_number, destination in poizdi:
        print(f"Номер поїзда: {train_number}, Призначення: {destination}")
    else:
      print("На станції в цей час немає поїздів.")
  elif option == "5":
    break
  else:
    print("Некоректний вибір. Спробуйте ще раз.")
