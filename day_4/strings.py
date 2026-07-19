1
x = ["Thirty", "Days", "Of", "Python"]
result = " ".join(x)
print(result)

2
x = ["Coding", "For", "All"]
result = " ".join(x)
print(result)

3
company = "Coding For All"

4
print(company)

5
print(len(company))

6
print(company.upper())

7
print(company.lower())

8
print(company.capitalize())
print(company.title())
print(company.swapcase())

9
print(company[:6])

10
print("Coding" in company)

11
r = "Coding For All"
print (r.replace("Coding", "Python"))

12
c = "Python for Everyone"
print (c.replace("Everyone", "All"))

13
r = "Coding For All"
print(r.split(" "))

14
media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(media.split(", "))

15
i = "Coding For All"
print(i[0])

16
print(i[13])

17
print(i[10])

18
P = "Python For Everyone"
PFE = P[0] + P[7] + P[11]
print(PFE)


19
C = "Coding For All"
CFA = C[0] + C[7] + C[11]
print(PFE)

20
c = "Coding For All"
print(c.index("c"))

21
F = "Coding For All"
print(F.index("F"))

22
f = "Coding For All People"
print(f.rfind("l"))

23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

24
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))

25
sentence = "You cannot end a sentence with because because because is a conjunction"
p = sentence[31:54]

26
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

27
sentence = "You cannot end a sentence with because because because is a conjunction"
p = sentence[31:54] 

28
y = "Coding For All"
print(y.startswith("Coding"))

29
y = "Coding For All"
print(y.endswith("coding"))

30
c = " Coding For All "
print(c.strip())

31
p = "30DaysOfPython"
c = "thirty_days_of_python"
print(c.isidentifier())
print(p.isidentifier())

32
d = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(d))

33
print("I am enjoying this challenge. \nI just wonder what is next.")

34
id = "Name\tAge\tCountry\tCity"
ids = "Asabeneh\t250\tFinland\tHelsinki"
print(id.expandtabs())
print(ids.expandtabs())

35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

36
a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))



























