#1
tupl = ()

#2
brothers = ("Louis",)
sisters = ("Susan",)

#3
siblings = brothers + sisters
print(siblings)

#4
print(len(siblings))

#5
family_members = siblings + ("Mom", "Dad")

#Level 2
#1
brother, sister, mom, dad = family_members
print(brother, sister, mom, dad)
#2
fruits = ("apple", "blueberry", "rasberry")
vegetables = ("squash", "eggplant", "cucumber")
animal_products = ("steak", "eggs", "hide")
food_stuff_tp = fruits + vegetables + animal_products

#3
food_stuff_lt = list(food_stuff_tp)

#4
print(food_stuff_lt[4:5])

#5
print(food_stuff_lt[:3])
print(food_stuff_lt[6:])

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


                
