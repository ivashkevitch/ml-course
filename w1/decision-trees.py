# coding=utf-8
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

pd.set_option('display.width', 200)
np.set_printoptions(linewidth=200)

# Загрузите выборку из файла titanic.csv с помощью пакета Pandas.
data = pd.read_csv('titanic.csv', index_col='PassengerId')

# Оставьте в выборке четыре признака:
# класс пассажира (Pclass), цену билета (Fare), возраст пассажира (Age) и его пол (Sex).
objectsAttributes = ['Pclass', 'Fare', 'Age', 'Sex']
objectsRaw = data[objectsAttributes]

# Обратите внимание, что признак Sex имеет строковые значения.
sexMap = {'male': 1, 'female': 0}
objectsRaw = objectsRaw.replace({'Sex': sexMap})

# Выделите целевую переменную — она записана в столбце Survived.
decisionsRaw = data['Survived']

# В данных есть пропущенные значения — например, для некоторых пассажиров неизвестен их возраст.
# Такие записи при чтении их в pandas принимают значение nan.
# Найдите все объекты, у которых есть пропущенные признаки, и удалите их из выборки.
objects = objectsRaw.dropna()
decisions = decisionsRaw[objects.index]


# Обучите решающее дерево с параметром random_state=241 и остальными параметрами по умолчанию
# (речь идет о параметрах конструктора DecisionTreeСlassifier).
clf = DecisionTreeClassifier(random_state=241)
clf.fit(np.array(objects), np.array(decisions))

# Вычислите важности признаков и найдите два признака с наибольшей важностью.
# Их названия будут ответами для данной задачи
# (в качестве ответа укажите названия признаков через запятую или пробел, порядок не важен).
attributesAndImportance = pd.DataFrame(
    np.array([objectsAttributes, clf.feature_importances_]).transpose(),
    columns=['Attributes', 'Importance']
)
attributesAndImportance['Importance'] = attributesAndImportance['Importance'].apply(pd.to_numeric)

print attributesAndImportance.nlargest(2, 'Importance')
