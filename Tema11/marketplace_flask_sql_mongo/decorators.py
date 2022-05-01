from functools import wraps


def decorator_function(orifinal_function):
    def wrapper_function():
        print(f"wrapper-ul")