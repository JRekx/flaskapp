from flask import Flask, request 
from operations import add,sub,mult,div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add both a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = add(a,b)

    return str(result)

@app.route("/sub")
def do_sub():
    """BOTH A,B ARE SUBTRACTED"""
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = sub(a,b)

    return str(result)

@app.route("/mult")
def do_mult():
    """BOTH A,B ARE MULTIPLIED"""
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = mult(a,b)

    return str(result)

@app.route("/div")
def do_div():
    """BOTH A,B ARE divided"""
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = div(a,b)

    return str(result)

operators = {
    "add" : add,
    "sub" : sub,
    "div" : div,
    "mult": mult, 
}

@app.route("/math<oper>")
def do_math(oper):
    """DOES MATH ON A AND B"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a,b)

    return str(result)