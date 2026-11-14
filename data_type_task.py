# a = 10
# b = 10.1555
# c = "Aishwarya"
# d = [10,20,30,40]
# e = {10,20,30,40}
# f = {"name":"Aishwarya","age":20}
# g = True
# h = None
# i = (10,20,30,40)
# j = 3 + 4j
# print(type(a))
# print(type(b))
# print(type(c))  
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# print(type(i))
# print(type(j))


# a = 10
# print(type(a))
# a = "Aishwarya"
# print(type(a))


# emp_id = 101
# emp_name = "Aishwarya"
# emp_salary = 25000.50
# department = "IT"
# status = True
# print(type(emp_id))
# print(type(emp_name))
# print(type(emp_salary))
# print(type(department))
# print(type(status)) 


# length = 10
# bredth = 20
# area = length * bredth
# print("Area of rectangle:", area)
# print(type(area))
# print(type(length))
# print(type(bredth))

# a = 10
# b = 20.5
# c = "30"
# print(type(a + b))
# print(type(str(a)))
# print(type(float(c)))


# a = "250"
# b = int(a)
# print(b * b)

# a = 45
# print(float(a))
# print(str(a))
# print(bool(a))


# a = 99.99
# b = int(a)
# print(b)
# # output Explanation : output is 99 because int()functions removes the decimal part of the number.


# a = "87"
# b = int(a)
# print(b)
# print(type(b))


# marks = 90
# marks = int(marks)
# Percentage =(marks / 100 )* 100
# print("Percentage =", Percentage)


# a = 100
# b = 30.5
# print(str(a) + str(b))
# print(int(b))
# print(float(a))
# print(bool(0))
# print(bool(""))


# name = "Aishwarya"
# print(name.upper())
# print(name.lower())


# a = "Aishwarya"
# print(len(a))


# a = "Python Programming"
# rev = ""
# for i in a:
#     rev = i + rev
# print(rev)

# a = "banana"
# count = 0
# for i in a:
#     if i == "a":
#         count += 1
# print(count)


# a = "I like Mango"
# b = a.replace(" ","-")
# print(b)

# a = "I like Mango"
# if "like" in a:
#     print("Yes")
# else:
#     print("No")
    
    

# email = "raneaishwarya@gmail.com"
# a = email.split("@")
# print("Username=", a[0])
# print("Domain=", a[1])



# name = "Aishwarya"
# age  = 21
# city = "Pune"
# print(f"My name is {name}. I am {age} years old and I live in {city}.")


# a = [10,60,30,80,45,90,20,55,70,15,65,40,100,25,85]
# for i in a:
#  if i > 50:
#      print(i)    


# a = [10,50,30,90,70]
# a.sort()
# print(a[-2])

# a = [10,20,10,30,20,40]
# b = []
# for i in a :
#     if i not in b:
#         b.append(i)
# print(b)


# a = [10,20,30]
# b = [40,50,60]
# c = a + b
# print(c)



# a = [10,20,30,40]
# b = [30,40,50,60]
# for i in a:
#     if i in b:
#         print(i)


# marks = [35,60,80,25,45,90]
# count = 0
# for i in marks:
#     if i >= 40:
#         count = count + 1
# print("Passed Students =", count)



# a = [10,-5,0,20,-10,0,5]
# positive = []
# negative = []
# Zero = []
# for i in a:
#     if i > 0:
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)      
#     else:
#         Zero.append(i)
# print("Positive Numbers:", positive)
# print("Negative Numbers:", negative)
# print("Zero Numbers:", Zero)


# a = [10,15,20,25,30]
# total = 0
# for i in a:
#     if i % 2 == 0:
#         total = total + i
# print(total)


# a = [
#     ["Rahul",80],
#     ["Disha",90],
#     ["Rohit",75],
# ]
# print(a[0][0])
# print(a[0][1])

# print(a[1][0])
# print(a[1][1])

# print(a[2][0])
# print(a[2][1])



# a = [10,20,30,40,50,60]
# rev = []
# for i in a :
#     rev.insert(0,i)
# print(rev)


# numbers =(10,25,55,60,45,80,90,30,87,97,67,43,98,75,78)
# for i in numbers:
#     if i >50:
#         print(i)


# a = (10,60,38,29,69,45)
# b = sorted(a)
# print(b[-2])




# a = (10,20,10,30,20,40)
# b = tuple(set(a))
# print(b)
 
 
# a = (10,15,30)
# b = (20,30,40)
# c = a + b
# print(c)


# a = (10,20,30,40)
# b = (30,40,50,60)
# for i in a:
#     if i in b:
#         print(i)


# marks = (75,76,34,54,85,96,45,30,90)
# count = 0
# for i in marks:
#     if i >= 40:
#         count = count + 1
# print(count)



# a = (10,-5,0,40,60,-35,0,68,-90,0)
# positive = []
# negative = []
# zero = []
# for i in a:
#     if i > 0:
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)
#     else:
#         zero.append(i)
# print(tuple(positive))
# print(tuple(negative))
# print(tuple(zero))



# a = (10,15,20,25,30,69)
# total = 0 
# for i in a:
#     if i % 2 == 0:
#         total = total + i
# print(total)


# a = (
#     ("Aishwarya", 80),
#     ("Disha", 90),
#     ("Vurjita", 70),
# )
# print(a[0][0])
# print(a[0][1])
# print(a[1][0])
# print(a[1][1])
# print(a[2][0])
# print(a[2][1])




# a = (10,20,30,40,50)
# rev = ()
# for i in a:
#     rev = (i,) + rev
# print(rev)



# a = {103,107,109,112}
# b = {102,104,106,112}
# print(a.intersection(b))



# a = {10,20,30,40}
# b = {30,40,50,60}
# print(a.difference(b))



# a = {10,20,30}
# b = {10,20,30,40,50}
# print(a.issubset(b))


# a = "Pineapple"
# b = set(a)
# print(b)




# a = {10,20,30,40}
# b = {20,30,50}
# c = {20,30,60}
# print(a.intersection(b.c))



# emp = {
#     "Mahendra": 24000,
#     "Riya": 37000,
#     "Amit": 28000,
#     "Shreya": 60000,
# }
# print(emp)



# emp = {
#     "Mahendra": 24000,
#     "Riya": 37000,
#     "Amit": 28000,
#     "Shreya": 60000,
# }
# higest = max(emp,key=emp.get)
# print(higest)
# print(emp[higest])



# emp = {
#     "Mahendra": 24000,
#     "Riya": 37000,
#     "Amit": 28000,
#     "Shreya": 60000,
# }
# total = 0
# for i in emp:
#     total = total + emp[i]
# print(total)



# a = "banana"
# d = {}
# for i in a:
#     if i in d:
#         d[1] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)



# keys = ["name","age","city"]
# values = ["Aishwarya",22,"pune"]
# c = dict(zip(keys, values))
# print(c)



# a = {"name":"Aishwarya","age":22}
# b = {"city":"Pune","salary":30000}
# a.update(b)
# print(a)


# products = {
#     "mobile":35000,
#     "mouse": 500,
#     "keyboard": 1000,
#     "pen": 10,
#     "bag": 550
# }
# for i in products:
#     if products[i]> 500:
#      print(i,products[i])



# students = {
#     "students1": {
#         "name": "Rahul",
#         "marks": 90
# },
#     "students2":{
#         "name":"Shweta",
#         "marks": 80
# },
#     "students3":{
#         "name":"Amit",
#         "marks": 70
# }
# }
# for i in students:
#     print(students[i])


    
    
# student = {
#     "name":"rahul",
#     "age":22,
#     "city":"pune"
# }
# if"age" in student:
#     print("key exists")
# else:
#     print("key not found")



# marks = {
#     "python": 78,
#     "java":90,
#     "SQL":80
# }
# highest = max(marks,key=marks.get)
# print("highest subject:-",highest)
# print("Marks:-",marks[highest])