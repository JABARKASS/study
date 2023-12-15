import matplotlib.pyplot as plt
import json

file_name = 'football_scores.json'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        sorted_data = sorted(data, key=lambda x: x['очки'], reverse=True)
        top_3_teams = sorted_data[:3]

        labels = [team['назва'] for team in top_3_teams]
        sizes = [team['очки'] for team in top_3_teams]
        colors = ['#9c3b3b', '#3b9c7f', '#6c3b9c']

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')

        plt.title('Розподіл очок серед топ-3 команд')
        plt.show()

except FileNotFoundError:
    print("Файл не знайдено.")