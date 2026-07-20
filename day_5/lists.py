#1
lst = []

#2
lst = ["x", "y", "z", "h", "l", "m"]

#3
print(len(lst))

#4
print(lst[0])
print(lst[2])
print(lst[4])

#5
mixed_data_types = ["Christian", 20, 5.11, "Single", "Mercersburg"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print(it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

#10
it_companies[0] = "Snapchat"
print(it_companies)

#11
it_companies.append("Meta")

#12
it_companies.insert(4, "Claude")

#13
it_companies[8] = it_companies[8].upper()

#14
print("#;  ".join(it_companies))

#15
does_exist = "Snapchat" in it_companies
print(does_exist)

#16
it_companies.sort()

#17
it_companies.reverse()

#18
print(it_companies[:3])

#19
print(it_companies[6:])

#20
print(it_companies[4:5])

#21
del it_companies[0]

#22
del it_companies[3:5]

#23
it_companies.pop()

#24
it_companies.clear()

#25
del it_companies 

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
code = front_end + back_end
print(code)

#27
variable_full_stack = code.copy()
variable_full_stack.insert(5, "Python")
variable_full_stack.insert(6, "SQL")
print(variable_full_stack)

#Start of Part 2

#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_ages = min(ages)
max_ages = max(ages)
print(min_ages)
print(max_ages)

ages.append(min(ages))
ages.append(max(ages))

ages.sort()
x = ages[5] + ages[6]
median = x / 2
print(median)

average = sum(ages) / len(ages)
print(f"{average:.2f}")

age_range = max(ages) - min(ages)
print(age_range)

x = abs(min(ages) - average)
b = abs(max(ages) - average)
print(x, b)





