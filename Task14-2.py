import csv
import matplotlib.pyplot as plt

# Зчитування даних з CSV-файлу
file_path = 'data.csv'

# Створення списку для зберігання даних
data = []

with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)  # Зчитування заголовків
    for row in csv_reader:
        data.append(row)

# Вивід доступних країн
countries = set(row[0] for row in data)
print("Доступні країни:", ', '.join(countries))

# Введення країн для побудови графіка
selected_country_1 = input("Введіть назву першої країни: ")
selected_country_2 = input("Введіть назву другої країни: ")

# Знаходження індексів колонок для вибраних країн
country_index = header.index("Country Name")
years_index = header.index("2002 [YR2002]")

# Знаходження даних для обраних країн
data_country_1 = [row for row in data if row[country_index] == selected_country_1][0]
data_country_2 = [row for row in data if row[country_index] == selected_country_2][0]

years = header[years_index:]
values_country_1 = data_country_1[years_index:]
values_country_2 = data_country_2[years_index:]

# Сортування значень за роками
sorted_values_country_1 = sorted(zip(years, map(float, values_country_1)))
sorted_values_country_2 = sorted(zip(years, map(float, values_country_2)))

# Розпакування відсортованих значень
sorted_years, sorted_values_country_1 = zip(*sorted_values_country_1)
_, sorted_values_country_2 = zip(*sorted_values_country_2)

# Побудова графіка для вибраних країн
plt.figure(figsize=(10, 5))
plt.plot(sorted_years, sorted_values_country_1, marker='o', label=selected_country_1, linestyle='-', color='b')
plt.plot(sorted_years, sorted_values_country_2, marker='o', label=selected_country_2, linestyle='-', color='r')
plt.title('Динаміка показника за роками')
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.legend()
plt.show()

# Побудова стовпчастої діаграми для обраних країн
plt.figure(figsize=(10, 5))
bar_width = 0.35
bar_positions_1 = range(len(sorted_years))
bar_positions_2 = [pos + bar_width for pos in bar_positions_1]
plt.bar(bar_positions_1, sorted_values_country_1, width=bar_width, label=selected_country_1, color='b')
plt.bar(bar_positions_2, sorted_values_country_2, width=bar_width, label=selected_country_2, color='r')
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.title('Стовпчаста діаграма для обраних країн')
plt.xticks([pos + bar_width / 2 for pos in bar_positions_1], sorted_years)
plt.legend()
plt.show()