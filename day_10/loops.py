#1 
for numbers in range(11):
 print(numbers)

number = 0
while number <= 10:
  print(number)
  number += 1

#2
for numbers in range(10,-1,-1):
  print(numbers)
 

number = 10
while number >= 0:
  print(number)
  number -= 1

#3
for i in range(1,8):
  print("#" * i)

#4
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()

#5
number = 0

while number <= 10:
  print(f"{number} X {number} = {number * number}")
  number = number +1

for number in range(11):
  print(f"{number} x {number} = {number * number}")

#6
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']

for language in languages:
  print(language)

#7
for number in range(101):
  if number % 2 == 0:
    print(number)

#8
for number in range(101):
  if number % 2 != 0:
    print(number)

#Level 2
#1
total = 0
for number in range(101):
  total += number
  print(f"The sum of all numbers is {number}.")

#2
even_total = 0
odd_total = 0

for number in range(101):
  if number % 2 == 0:
    even_total += number
  else:
    odd_total += number
print(f"The total of even numbers is {even_total}.")
print(f"The total of odd numbers is {odd_total}.")

#Level 3
#1
from countries import countries

for country in countries:
  if "land" in country:
    print(country)
    
#2
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
  reversed_fruits.insert(0, fruit)
print(reversed_fruits)

#3
#i
from countries_data import countries

language_set = set()

for country in countries:
  if "languages" in country:
    language_set.update(country["languages"])
print(len(language_set))

#ii
from countries_data import countries
language_list = []
for country in countries:
  if "languages" in country:
    language_list.extend(country["languages"])
print(language_list)

counts = {}
for language in language_list:
    if language in counts:
        counts[language] = counts[language] + 1
    else:
        counts[language] = 1

#iii
populations = []
for country in countries:
  populations.append((country["population"], country["name"]))
populations.sort()
print(populations[-10:])
      
    
  
  













