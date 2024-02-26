from flask import Flask , render_template , jsonify
from flask import request
import math

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods = ['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = 'The Sum Of   ' + str(num1) + '  and  ' + str(num2) + '  is  ' + str(r)
        if(ops == 'subtract'):
            r = num1 - num2
            result = 'The Subtract Of   ' + str(num1) + '  and  ' + str(num2) + '  is  ' + str(r)
        if(ops == 'multiply'):
            r = num1 * num2
            result = 'The Multiply Of   ' + str(num1) + '  and  ' + str(num2) + '  is  ' + str(r)
        if(ops == 'divide'):
            r = num1 / num2
            result = 'The Divide Of   ' + str(num1) + '  and  ' + str(num2) + '  is  ' + str(r)
        if(ops == 'log'):
            r = math.log(num1 , num2)
            result = 'The Log Of   ' + str(num1) + '  and  ' + str(num2) + '  is  ' + str(r)
        return render_template('results.html', result = result)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=8000)