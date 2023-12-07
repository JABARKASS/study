# Завдання а
def create_file(filename, content):
  try:
      with open(filename, 'w') as file:
          file.writelines(content)
      print(f"Файл {filename} успішно створено.")
  except Exception as e:
      print(f"Помилка при створенні файлу {filename}: {e}")

# Завдання б
def process_file(input_filename, output_filename):
      try:
          with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
              for line in input_file:
                  processed_line = ''.join(['1' if char == '0' else '0' if char == '1' else char for char in line])
                  output_file.write(processed_line[:15] + '\n')

          print(f"Файл {output_filename} успішно створено.")
      except Exception as e:
          print(f"Помилка при обробці файлів: {e}")

# Завдання в
def print_file_content(filename):
  try:
      with open(filename, 'r') as file:
          for line in file:
              print(line.strip())
  except Exception as e:
      print(f"Помилка при читанні файлу {filename}: {e}")

# Завдання а
create_file('TF23_1.txt', ["Рік номер 1.\n", "Речення.\n", "Одиниця виглядає як 1.\n", "Чи не схожий 0 на 8?\n"])

# Завдання б
process_file('TF23_1.txt', 'TF23_2.txt')

# Завдання в
print("Вміст файла TF23_2:")
print_file_content('TF23_2.txt')