#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # This will print the string to the console
    return f'<p>{text}</p>'

@app.route('/count/<int:number>')
def count(number):
    numbers_list = '\n'.join(str(i) for i in range(number + 1))
    return f'<pre>{numbers_list}</pre>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<p>Error: Division by zero</p>'
    elif operation == '%':
        result = num1 % num2
    else:
        return '<p>Error: Invalid operation</p>'

    return f'<p>Result: {result}</p>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
