# def func1(func):
#     print("Я func1")
#     return func()

# def func2():
#     print("Я func2")
#     return "hello"
# print
# res = func1(func2)
# print(res)
# def empty_decorator(func):
#     return func
# def get_hello():
#     return "Hello"
# hello = empty_decorator(func = get_hello)
# print(hello())

# def to_uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
# @to_uppercase
# def  get_text():
#     return "Hello world"
# @to_uppercase
# def get_full_name():
#     return "John Snow"

# res_text = to_uppercase(get_text)
# res_fullname  = to_uppercase(get_full_name)
# print(get_text())
# print(get_full_name())
# print(get_text())
# print(get_full_name())

def strong(func):
    def wrapper():
        return '<strong>' + func() + '<strong>'
    return wrapper

def div(func):
    def wrapper():
        return '<div>' + func() + '<div>' 
    return wrapper
@div
@strong
def get():
    return "John Snow"

print(get ())

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f"Trace: вызвана {func.__name__}()\n {args} {kwargs}")
#         original_result = func(*args, **kwargs)
#         print(f'Trace:вызвана {func.__name__}()\n вернула {original_result}')
#         return original_result
#     return wrapper

# @trace
# def say(name, line):
#     return f"{name}: {line}"
# say("John", "Hello world")



# def hello_makers ():
#     print ("Hello makers")

# # Хранить функцию в переменных

# makers = hello_makers
# # print(makers())
# makers()

# Определять функции внутри другой функции
 
# def outer_func():
#     def inner_func():
#         print("Hello!")
#     inner_func()
# outer_func()


# Передавать функции в увчестве аргумета и возвращать их из других функций
# def main_func(func):
#     print(f"Got {func} thank you")
#     func()
#     return func

# def hello_makers ():
#     print ("Hello makers")

# main_func(hello_makers)