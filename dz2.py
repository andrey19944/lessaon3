name = input('Ведите имя:')
surname = input('Ведите фамилию:')
year = int(input('Ведите год:'))
city = input('Ведите город:')
email = input('Ведите email:')
telephone = input('Ведите номер телефоно:')

def my_func (name, surname, year, city, email, telephone):
      return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Мякошин', name = 'Андрей', year = '1994', city = 'Раменское', email = 'Sirotka122@icloud.com', telephone = '89254142669'))