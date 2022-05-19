from flask import Flask

app = Flask(__name__)  # __name__ is var w/ name of current module/script being executed, __main__ refers to this file


def make_bold(function):
    def wrapper():
        return '<b>' + function() + "</b>"
    return wrapper


def make_italicized(function):
    def wrapper():
        return '<em>' + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return '<u>' + function() + "</u>"
    return wrapper


def make_h1(function):
    def wrapper():
        return f'<h1>' + function() + f'</h1>'
    return wrapper


def make_h2(function):
    def wrapper():
        return f'<h2>' + function() + f'</h2>'
    return wrapper


def make_h3(function):
    def wrapper():
        return f'<h3>' + function() + f'</h3>'
    return wrapper


@app.route('/')  # Decorator ensures function only triggers if user tries to access the URL '/' (homepage))
@make_bold
@make_h1
def hello_world():
    # Can directly return HTML and CSS
    return 'Hello, world!'


@app.route('/bye')  # Triggers when user goes to 'homepage_url/bye'
def say_bye():
    return 'Bye'


@app.route('/<name>/<int:number>')  # Receives <name> input as an argument and number as an int argument
def greet(name, number):
    return f'Hello {name}, your number is {number}!.'

# To use this as a server:
# 1. Go to terminal
# 2. Enter 'set FLASK_APP=hello.py' (sets FLASK_APP environment variable to this file
# 3. Enter 'flask run'


# Actually just run it
if __name__ == "__main__":
    app.run(debug=True)



