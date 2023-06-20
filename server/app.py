#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/hello') 
def greeting():
     print('hello')
     return 'hello'
@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(num) for num in range(param)) + '\n'
    return numbers
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
     if operation == '+':
        result = 5 + 5
     elif operation == '-':
        result = num1 - num2
     elif operation == '*':
        result = num1 * num2
     elif operation == 'div':
        result = num1 / num2
     elif operation == '%':
        result = num1 % num2

     if result is None:
        return 'Invalid operation or division by zero.'
     else:
      return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
