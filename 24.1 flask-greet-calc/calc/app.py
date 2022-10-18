from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_func():
    """Add a and b parameters."""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)

    return str(result)

@app.route("/sub")
def sub_func():
    """Subtract and b parameters."""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def mult_func():
    """Multiply a and b parameters."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)

    return str(result)

@app.route("/div")
def div_func():
    """Divide a and b parameters."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)

    return str(result)



# FURTHER STUDY

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<oper>")
def math(oper):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations[oper](a,b)
    
    return str(result)
