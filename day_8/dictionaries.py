#1
dog = {}

#2
dog = {"name" : "maxwell", "breed" : "westy", "legs" : "long", "color" : "white", "age" : "14"}

#3
student = {
  "first_name" : "Christian", 
  "last_name" : "Concordia", 
  "gender" : "male", 
  "marital_status" : "single", 
  "skills" : ["Soccer", "Lifting", "Phython"], 
  "age" : "20",
  "country" : "USA", 
  "city" : "mercersburg", 
  "address" :{
      "street" : "Everett",
      "zipcode" : "10346"}
}

#4
print(len(student))

#5
x = student["skills"]
print(type(x))

#6
student["skills"].append("singing")
print(student)

#7
keys = student.keys()
print(list(keys))

#8
values = student.values()
print(list(values))

#9
print(list(student.items()))


#10
student.pop("skills")

#11
del student




