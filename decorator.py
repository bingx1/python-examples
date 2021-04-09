from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


# This is 
def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

# Equivalent to 
@not_during_the_night
def say_whee():
    print("Whee!")

# Decorator is just syntactic sugar

def do_twice(func):
    #By using *args and *kwargs we can accept as as many positional/keyword args we want
    def wrapper_do_twice(*args, **kwargs): 
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

# Decorator also decides what to return from the function
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")

### Maintaining access control on API endpoints
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
