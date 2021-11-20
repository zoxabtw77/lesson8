# cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus', 'Termz', 'Namangan', 'Andijan']

# three_cities = cities[3:6]
# print(three_cities)
# print(three_cities)

# v obratnom poryadke 
# reversed_cities = cities[::-1]

#gorod est li v strake true/false with help 'in' tak j i ciframi
# print('Nukus' in cities)   

#print vsex gorodov iz spiska
# for city in cities:
#    print(city)

# print(range(10))
# (0, 1, 2, 3, 4, 5, 6, 7 , 8, 9)

# for num in range(10):
#     print(num)

#interebles
# 1.lists - []
# 2. temples ()
# 3. string - '', ""
# 4. range()

#ЦИКЛ FOR нужен для того, чтобы прогонять через цикл ИНТЕРИРУЕМЫЕ СУЩНОСТИ 

# for a in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
#     print(a * a,  a * a * a)

#range для работ с большыми цыфрами и списками !

#sum-acc acumuliruushaya num 
# acc = 1 
# for num in range(1, 11):
#     acc = acc * num 

#     print(acc)

# 0-20 только четные 
# sum = 0
# for num in range(0, 20, 2):
#     print(num)

cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus', 'Termz', 'Namangan', 'Andijan']
acc = ''
cities_len = len(cities)
for i in range(len(cities)):
  if i != len(cities) -1:
    acc += cities[i] + ','
else: acc += cities[i]
print(acc)