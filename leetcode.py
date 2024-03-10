# class GameCharacter:
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#
#     def speak(self):
#         print("Hi, my name is " + self.name)
#
#
# class Villain(GameCharacter):
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#
#     def speak(self):
#         print("Hi my name is " + self.name + " and i will kill you")
#
#     def kill(self, target):
#         target.health = 0
#         print(target.name + "'s Health = " + str(target.health) + "| Bang-bang, now you're dead")
#
#
# bob = GameCharacter("Bob", 100, 10)
# thanos = Villain("Thanos", 900, 100)
#
# bob.speak()
# print("")
# thanos.speak()
# thanos.kill(bob)




#
#
# list = [1,2,3,4,5,6,7]
#
#
# def finder(list):
#     empty_list = []
#     for x, y in enumerate(list):
#         for a, b in enumerate(list):
#             if list[x] + list[a] == 9:
#                 empty_list.append(x)
#                 empty_list.append(a)
#                 return empty_list
#     return 0
#
#
# print(finder(list))



# def test(*args):
#     malist = []
#     for i in args:
#         for x in i:
#             malist.append(x)
#     return malist
#
# print(test([1,2,3,4,5,6]))




# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# z = x.union(y)
#
# print(z)



# def palindrome(x):
#     reversed_number = 0
#
#     while x != 0:
#         digit = x % 10
#         reversed_number = reversed_number * 10 + digit
#         x //= 10
#     return reversed_number
#
# print(palindrome(1234))


# x = 1234
# print(type(int(str(x)[::-1])))


# def palindrome(x):
#     y = str(x)[::-1]
#     return True if str(x) == y else False
#
# print(palindrome(121))


#
# roman = {
#     'M' : 1000,
#     'CM' : 900,
#     'D' : 500,
#     'CD' : 400,
#     'C' : 100,
#
# }


import asyncio

# async def b1(x):
#     return x
# x = b1(32)
# async  def b2(y):
#         await x
#         return y
#
#
# print(asyncio.run(b2(22)))
# print(asyncio.run(x))



# number = int(input("Number to Roman : "))
#
# roman_list = {
#     'M' : 1000,
#     'CM' : 900,
#     'D' : 500,
#     'CD' : 400,
#     'C' : 100,
#     'XC' : 90,
#     'L' : 50,
#     'XL' : 40,
#     'X' : 10,
#     'IX' : 9,
#     'V' : 5,
#     'IV' : 4,
#     'III' : 3,
#     'II' : 2,
#     'I' : 1
# }
# result = ''
# for x, y in roman_list.items():
#         if (number - y) > 0:
#             number = number - y
#             result+=x
#
#
#
# print(result)

# def print_args(func):
#     def wrapper(*args, **kwargs):
#         print(args)
#         func(*args)
#     return wrapper
#
# @print_args
# def func(x, y):
#     print(x * y)
#
# func(5, 9)


