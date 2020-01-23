'''
Credits: TeamTreeHouse

part 1
-------
1. we call the flask script an app
2. the app is where all the requests come to
3. the app then sends those requests to the correct function or 'view'
4. it finds those functions through the 'route'
5. the view then sends back a response
6. we call this the 'request-response cycle'
7. views can have more than one route
8. the routes start with a forward slash

part 2
------
1. lots of times we want to let users send in arguments and values through the url
2. the most common way of doing this is by using query strings

part 3
-------
1. The query string begins after the question mark (?) and has two key-value pairs separated by an ampersand (&). 
For each pair, the key is followed by an equals sign (=) and then the value. 
example: example.com?arg1=value1&arg2=value2
2. query strings is not the nicest way to pass arguments.
3. there is another way to it
4. int objects are not callable in flask
'''

from flask import Flask
from flask import request

# below code indicates to use the current namespace
# if we were to run simple_app.py directly, the namespace would be __main__ meaning it's running directly
# if we were to import simple_app to another file, then the namespace would be simple_app
app = Flask(__name__) 

# to make a normal function a view, we have to give it a route
# to give route, we decorate it with the function @app.route and specify what the route is
# a decorator is a function that wraps around another function and lets you do things to that function
@app.route('/') # example query string: http://127.0.0.1:5000/?name=neeraj
def index(name="World"):
    # args object holds all the arguments in the request
    # it's like a dictionary, so we can use the get method
    name = request.args.get("name", name)
    return "Hello {}".format(name)

# flask captures whatever comes after the forward slash and within the brackets as an argument
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    return "{} + {} = {}".format(num1, num2, num1 + num2)

# debug=True means anytime we make changes, flask auto restarts
# port is like having many doors in a house, and which door you're gonna be at
# host is like which house is it on the street
app.run(debug=True, port=5000, host='localhost')
