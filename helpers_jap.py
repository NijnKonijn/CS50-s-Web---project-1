"""
http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/

This example assumes that the login page is called 'login' and that the current user is stored in g.user and is None if there is no-one logged in.

from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
To use the decorator, apply it as innermost decorator to a view function. When applying further decorators, always remember that the route() decorator is the outermost.
"""

from functools import wraps
from flask import request, redirect, url_for, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function