

#  -------------------------------------------lists --------------------------------------------
# print("Enter 5 numbers : ")
# numbers = [input("Enter a number :") for _ in range(5)]
1
# print(numbers)
# print(numbers[0])

# num = list([[input("Enter a number :")for _ in range(3)] for _ in range(3)])
# print(num)

# for i in range(3):
#     for j in range(3):
#         print(num[i][j], end=" ")
#     print()


#  -------------------------------------------sets --------------------------------------------


# a = {1, 2, 3}
# b = {3, 4, 5}


# print(a ^ b)   # {1, 2, 4, 5}


# -------------------------------------------tuples --------------------------------------------

# t =(1,2,3,1,7,3)
# print(t)
# print(t[1])

# for items in t:
#     print(items, end=" ")


# def min_max(num):
#     return (min(num), max(num))

# results = min_max([1, 2, 3, 4, 5])
# print(results)




# for i in pairs:
#     if i[1] > i[0]:
#         print(i, end="   ")

# pairs = [(1, 2), (3, 4), (2, 3), (9,11)]

# for i, j in enumerate(pairs):
#     if j[1] > j[0]:
#         print(f"Pair {i}: {j}", end="   ")  


#-#  -------------------------------------------dictionaries --------------------------------------------

# dic = {
#     "name": "Abdul Basit",
#     "age":22,
#     "city":"Lahore"
# }

# print(dic)

# student = dict(name = "Abdul", age =22)
# print(student)
# student = dict(name = "ahmad", age =22, city = "Lahore")
# print(student)

# if "ahmad" in student.values():
#     print("Yes Exists")


# person = {"name": "Ali", "city": "Lahore"}


# for k, v in person.items():
#     print(f"{k} => {v}")


# names = ["Ali", "Maria", "Ali", "Ahmed", "Maria", "Ali"]
# dict = {}

# for name in names:
#     if name in dict:
#         dict[name] += 1
#     else:
#         dict[name] = 1

# print(dict)



# names = ["Ali", "Maria", "Ali", "Ahmed", "Maria", "Ali"]

# # Create empty dictionary to store counts
# name_counts = {}

# # Loop through each name
# for name in names:
#     if name in name_counts:
#         name_counts[name] += 1  # Increment if exists
#     else:
#         name_counts[name] = 1   # Initialize if new

# print(name_counts)



new = set()

new.add((1,2))

print(new)