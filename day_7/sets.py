# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))

#2
it_companies.add("Twitter")

#3
it_companies.update["Meta", "Google"]

#4
it_companies.remove("Google")

#5
# if the item being removed isnt found, discard wont raise any erros whereas removew will\

# Level 2
#1
print(A.union(B))

#2
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
A.update(B)
print(A)
B.update(A)
print(B)

#6 
print(A.symmetric_difference(B))

#7
del A
del B
del age
del it_companies

#Level 3
#1
ages = set(age)
print(len(ages))
print(len(age))

#2
#tuple is unmoddifiable, sets are unordered and unindexed, lists are ordered, and a string is a specific set of letters it is not like the other 3

#3
x = "I am a teacher and I love to inspire and teach people".split()
p = set(x)
print(len(p))
