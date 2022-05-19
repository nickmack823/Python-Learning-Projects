import time


# Decorater Function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Add functionality before
        function()
        # Add functionality after
    return wrapper_function()


@delay_decorator  # Decorates below function with above decorator
def say_hello():
    print('Hello')


def say_bye():
    print('Bye')


def say_greeting():
    print('How are you?')


say_hello
# Alternative to the @ method
# decorated_function = delay_decorator(say_greeting())
# decorated_function