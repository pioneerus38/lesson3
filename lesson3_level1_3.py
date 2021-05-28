import collections
import operator
from functools import reduce

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
name_cntr = collections.Counter()
for student in students:
    name_cntr[student['first_name']] += 1
name_dict = dict(name_cntr)
name_list = sorted(name_dict)
for name in name_list:
    print(f'{name}: {name_dict[name]}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
name_cntr = collections.Counter()
for student in students:
    name_cntr[student['first_name']] += 1
mc_name = name_cntr.most_common(1)
print(f'Самое частое имя среди учеников: {mc_name[0][0]}')


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
name_cntr = collections.Counter()
name_list = []
for school_class in school_students:
    for student in school_class:
        name_cntr[student['first_name']] += 1
    name_list.append(name_cntr.most_common(1))
    name_cntr.clear()
for index, name in enumerate(name_list, start=1):
    print(f'Самое частое имя в классе {index}: {name[0][0]}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for school_class in school:
    male = reduce(lambda x, y: x + is_male.get(y['first_name']), school_class['students'], 0)
#    male = 0
#    for student in school_class['students']:
#        if is_male.get(student['first_name']):
#            male += 1
    print(f"В классе {school_class['class']} {len(school_class['students']) - male} девочки и {male} мальчика")            

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for school_class in school:
    male = reduce(lambda x, y: x + is_male.get(y['first_name']), school_class['students'], 0)
    school_class['male'] = male
    school_class['female'] = len(school_class['students']) - male
male_most = sorted(school, key=operator.itemgetter('male'), reverse=True)
print(f"Больше всего мальчиков в классе {male_most[0]['class']}")
female_most = sorted(school, key=operator.itemgetter('female'), reverse=True)
print(f"Больше всего девочек в классе {female_most[0]['class']}")

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a