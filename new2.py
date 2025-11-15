import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('author_ru_utf.csv')

#task 1
Gogol_df = df[df['Author'] == 'ГогольНВ']
service_pos_columns = ['на', 'что', 'за', 'и', 'в', 'из', 'со', 'а', 'во', 'для', 'с', 'но', 'к', 'по', 
                     'от', 'под', 'до', 'про', 'о', 'ко', 'над', 'без', 'при', 'об', 'через', 'из-за', 'из-под']
service_pos_sums = Gogol_df[service_pos_columns].sum()
most_common_service_pos = service_pos_sums.idxmax()
most_common_count = service_pos_sums.max()
print(service_pos_sums.sort_values(ascending=False).head())
# task2
prepositions = ['на', 'с', 'в']
for prep in prepositions:
    plt.figure(figsize=(10, 6))
    plt.hist(df[prep], bins=10, alpha=0.7)
    plt.title(f'Распределение предлога "{prep}" по всему датасету')
    plt.xlabel('Количество случаев')
    plt.ylabel('Частота')
    plt.show()

# task3
authors = df['Author'].unique()
data_for_boxplot = [df[df['Author'] == author]['из-за'].dropna() for author in authors]
plt.figure(figsize=(12, 6))
plt.boxplot(data_for_boxplot, labels=authors, vert=True)
plt.title('Распределение предлога "из-за" по авторам')
plt.xlabel('Авторы')
plt.ylabel('Количество предлога "из-за"')
plt.xticks(rotation=90) 
plt.tight_layout()
plt.show()

# task4
author1 = 'ГогольНВ'
author2 = 'ГончаровИА'
data_author1 = df[df['Author'] == author1]['за'].dropna()
data_author2 = df[df['Author'] == author2]['за'].dropna()
plt.figure(figsize=(10, 6))
plt.hist([data_author1, data_author2], bins=10, label=[author1, author2], alpha=0.7)
plt.title('Распределение предлога "за" у двух авторов')
plt.xlabel('Количество предлога "за"')
plt.ylabel('Частота')
plt.legend()
plt.show()