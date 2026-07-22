#1 
x = int(input("Enter your age: "))

if x >= 18:
  print("You are old enough to learn to drive.")
else:
  years_to_drive = 18 - x
  print(f"You need {years_to_drive} more years to learn to drive.")

#2
your_age = int(input("Enter your age: "))
my_age = 20

if your_age > my_age:
  older = your_age - my_age
  if older == 1:
    print(f"You are {older} year older than me.")
  else:
    print(f"You are {older} years older than me.")
elif your_age < my_age:
  print("You are younger than me")
else:
  print("We are the same age")

#3

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
  print("A is greater than B")
elif a < b:
  print("A is smaller than B")
else:
  print("A is equal to B")

#Level 2
#1
grade = int(input("Grade: "))

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

#2
month = input("Month: ")

Autumn = ["September", "October", "November"]

Winter = ["December", "January", "February"]

Spring = ["March", "April", "May"]

Summer = ["August", "June", "July"]

if month in Autumn:
  print("Autumn")
elif month in Winter:
  print("Winter")
elif month in Spring:
  print("Spring")
else:
  print("Summer")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Fruit: ")

if fruit in fruits:
  print("That fruit already exists in the list")
else:
  fruits.append(fruit)
  print(fruits)

#Level 3
#1
  person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
  print(person["skills"][2])

if "skills" in person:
  print("Python" in person["skills"])

skills = person["skills"]
if "JavaScript" in skills and "React" in skills and "Node" not in skills:
  print("He is a front end developer")
elif "Node" in skills and "Python" in skills and "MongoDB" in skills and "React" not in skills:
  print("He is a backend developer")
elif "React" in skills and "Node" in skills and "MongoDB" in skills and "Python" not in skills:
  print("He is a fullstack developer")
else:
  print("Unknown title")




if is_married is True and person["country"] == "Finland":
  print(f"{person["first_name"]} lives in {person["last_name"]}. He is married")




















              





