# def f1(x,func):
#     result = 1
#     for y in range(1, x):
#         result = result * func(y)
#     return result
#
# print(f1(4, lambda y : y * y))


# def decorator(func):
#     def wrapper(*args):
#         print("This is first wrapper text")
#         print(func(*args))
#         print("this is last wrapper text")
#         print("-----------------------")
#     return wrapper
#
#
# @decorator
# def fun(name):
#     return name
#
# @decorator
# def car(name, age):
#     return name +" "+ str(age)
#
#
# fun("Arman")
# car("Audi", 11)




# def decorator_factory(argument):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             result = 1 + function
#             return result
#         return wrapper
#     return decorator
#
# @decorator_factory(True)
# def dec()



