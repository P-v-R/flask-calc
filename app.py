from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_response():
    """responds the sum of two numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = add(a,b)
    return f"<h1>{result}</h1>"
 
@app.route('/sub')
def sub_response():
    """responds the result of two numbers subtracted"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = sub(a,b)
    return f"<h1>{result}</h1>"
 
@app.route('/mult')
def mult_response():
    """responds the result of two numbers multiplied"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = mult(a,b)
    return f"<h1>{result}</h1>"
 

@app.route('/div')
def div_response():
    """responds the result of two numbers divided"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = div(a,b)
    return f"<h1>{result}</h1>"
 


