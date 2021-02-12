some_string = "Hello world"

print(some_string.replace("world", "people"))
print(some_string)

some_string = some_string.replace("world", "people")
print(some_string)

print(some_string.replace(some_string[4:8], ""))

empty_string = ""
print(type(empty_string))

empty_list = []
print(type(empty_list))

empty_tuple = ()
print(type(empty_tuple))

# empty_set = {}
# print(type(empty_set))
#
# empty_set = set()
# print(type(empty_set))
#
#
# # some_list = [12345, 123.000, "Some string", True, None, [1234, "new string", False]]
# # print(some_list)
# # print(some_list [0])
# # print(some_list [0:4])
# # print(some_list [::2])
#
#
# some_coureses = [123456, 123.0006, "Some strinng", True, None, [1234, "new string", False]]
# print(some_coureses[5][2])
#
# coureses = ["history", "Math", "literature", "Physics", "Programming"]
# # print(len(coureses))
# coureses2 = ["Art", "Biology"]
# # print(coureses + coureses2)
# coureses.append("Art")
# print(coureses)
# coureses.append(coureses2)
# print(coureses)
# #
# # coureses[5].append(coureses2)
# # print(coureses)
# # print(coureses[5][2][1])
#
# # print(coureses)
# # coureses.remove("Math")
# # print(coureses)
# #
# # coureses.pop()
# # print(coureses)
# #
# # popped_item = coureses.pop()
# # print(popped_item)
# #
# #
# # coureses.insert(2, "biolifuy")
# # print(coureses)
#
# coureses = ["history", "Math", "literature", "Physics", "Programming"]
# numbers = [1, 45, 63, 34, 56, 78, 3]
# coureses2 = ["Art", "Biology"]
#
# print(numbers)
# numbers.sort()
# print(numbers)
#
# print(coureses)
# coureses.sort()
# print(coureses)
# #
# # print(coureses.sort(reverse=True))
# # print(coureses)
# # option = True
# # print(coureses.sort(reverse=option))
# print(coureses)
# print(sorted(coureses)) #формирует только один раз
# print(coureses)


# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
#
#
# print(coureses.index("Math"))
# print(coureses)
#
# print(coureses.index("Math"))
# math_index = coureses.index("Math")
# print(coureses[math_index])
#
#
# print(coureses)
# print("Art" in coureses) #узнает есть ли данный элемент в строке
#
# new_string ="***".join(coureses)
# print(new_string)
#
# new_string =", ".join(coureses)
# print(new_string)
# print(type(new_string))
#
#
# new_list = new_string.split(", ")
# print(new_list)
# print(type(new_list))


# list_1 = ["Math", "History", "Programming", "Physics"]
# list_2 = list_1.copy()
# list_2.append("Biology")
# print(list_1)
# print(list_2)
#
# list_1[2] = "Sports"
# list_2[0] = "Art"
#
# print(list_1)
# print(list_2)
#
# list_1 = ("Math", "History", "Programming", "Physics")
# print(list_1[2])
#
# coureses = ("history", "Math", "literature", "Physics", "Programming")
# coureses2 = ("Art", "Biology")
#
# coureses = coureses2 + coureses
# print(coureses)

#
# set1 = {"Math", "History", "Programming", "Physics", "Math"}
# set2 = {"Art", "Physics", "Design", "History"}
# # list_1 = ["Math", "History", "Programming", "Physics", "History"]
# #
# # print(list_1)
# # print(type(list_1))
# # print(list(set(list_1)))
#
# print(set1.intersection(set2))
#
# print(set2.difference(set1))
# print(set1.difference(set2))
#
# print(set1.union(set2))


# courses = ['Design', 'Art', 'Programming', 'Math', 'Physics', 'History']
#
# counter = 0
# for subject in courses:
#     print(subject)
#     counter += 1
# print(counter)


# courses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# counter = 0
# for num1 in courses:
#     for num2 in courses:
#         for num3 in courses:
#             for num4 in courses:
#                 print(num1, num2, num3, num4)

numbers = range(1, 100)
for num in numbers:
    if num %5 == 0 and num % 3 == 0:
        print(num, "FizzBuzz")
    elif num % 5 == 0:
        print(num, "Fizz")
    elif num % 3 == 0:
        print(num, "Buzz")

