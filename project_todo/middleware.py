from functools import wraps
from project_todo.jwt import JWTAuth
from project_todo.response import Response


def jwtRequired(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            decode(args[0].headers.get('Authorization'))
        except Exception as e:
            return Response.unauthorized()
        return fn(*args, **kwargs)

    return wrapper


def decode(token):
    token = str(token).split(' ')
    return JWTAuth().decode(token[1])