# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14silLSrpRR5IiBnAi-_oI4qPFo3onot6
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Seminar_10/data20152019.csv', sep=';', encoding='cp1251')

df = df.iloc[33:41, :]

df = pd.DataFrame(df, columns= ['Субъект РФ', 'Численность студентов, очная форма, человек, 2017'])

# Создаем график с помощью библиотеки Seaborn
sns.barplot(df, x='Субъект РФ', y='Численность студентов, очная форма, человек, 2017')

# Настраиваем оси и заголовок графика
plt.xlabel('Субъект РФ')
plt.ylabel('Численность студентов, очная форма, человек')
plt.title('Численность студентов по субъектам РФ (2017)')

# Поворачиваем подписи по оси X на 90 градусов, чтобы они не перекрывали друг друга
plt.xticks(rotation=90)

# Отображаем график
plt.show()