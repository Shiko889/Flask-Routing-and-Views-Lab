from flask import Flask

app = Flask(__name__)

@app.route ('/')
def  index():
    return "<h1> Python Operations with Flask Routing and Views  </h1>"

@app.route('/print/<string:str>')
def print_string(str):
    print(str)
    return str

@app.route('/count/<int:num>')
def count(num):
    numbers = "\n".join(str(i) for i in range(num+1))
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
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
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)