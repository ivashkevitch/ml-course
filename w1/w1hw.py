# coding=utf-8
import pandas as pd
import numpy as np
import re

pd.set_option('display.width', 200)
np.set_printoptions(linewidth=200)

data = pd.read_csv('titanic.csv', index_col='PassengerId')


# Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
print data['Sex'].value_counts()


# Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров.
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.

allPassengersCount = len(data)
survivorsCount = data['Survived'].value_counts()[1]
survivorsShare = round(100. * survivorsCount / allPassengersCount, 2)
print survivorsShare


# Какую долю пассажиры первого класса составляли среди всех пассажиров?
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.

firstClassCount = data['Pclass'].value_counts()[1]
firstClassShare = round(100. * firstClassCount / allPassengersCount, 2)
print firstClassShare


# Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.
# В качестве ответа приведите два числа через пробел.

ages = data['Age']
print round(ages.mean(), 2)
print ages.median()


# Коррелируют ли число братьев/сестер/супругов с числом родителей/детей?
# Посчитайте корреляцию Пирсона между признаками SibSp и Parch.

correlation = data['SibSp'].corr(data['Parch'])
print round(correlation, 2)


# Какое самое популярное женское имя на корабле?
# Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name).
# Это задание — типичный пример того, с чем сталкивается специалист по анализу данных.
# Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию.
# Попробуйте вручную разобрать несколько значений столбца Name и выработать правило для извлечения имен,
# а также разделения их на женские и мужские.


def parse_first_name(full_name):
    # первое слово в скобках
    inside_scope = re.search('.*\((\w+).*\).*', full_name)
    if inside_scope is not None:
        return inside_scope.group(1)
    # если нет - то вернуть первое слово после точки и пробела
    return re.search('.*\. (\w+).*', full_name).group(1)


females = data[data['Sex'] == 'female']
femalesFullNames = females['Name']
femalesFirstNames = femalesFullNames.apply(parse_first_name)
print femalesFirstNames.value_counts()[:1]

