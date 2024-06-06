my_dict = {'Marusya' : 1978, 'Alisa' : 2009, 'Viktor' : 1972, 'Aleksandra' : 2003}
print(my_dict)
my_dict['Marusya'] = 2006
print(my_dict['Marusya'])
my_dict['Oleg'] = 2003
print(my_dict)
# обращение к несуществующему ключу
my_dict['Valentina_Viktorovna'] = 1950
print(my_dict)
# или через метод update
my_dict.update({'Vladimir_Ivanovich' : 1949, 'irina' : 1969, 'Katya' : 1997, 'Sveta' : 1980})
print(my_dict)
del my_dict['Sveta']
print(my_dict)
print(my_dict.get('Vladimir_Ivanovich'))
v = my_dict.pop('Aleksandra')
print(my_dict)
print(v)
# множество
my_set = {'Aleksandra', True, 5101, 'Irina', 'Aleksandra', 5101, 12, 0.7, 12, True, 5101, 'Irina'}
print(my_set)
my_set.add(0.8)
print(my_set)