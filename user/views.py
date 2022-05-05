import json
from django.shortcuts import render
from project_todo.jwt import JWTAuth
from project_todo.middleware import jwtRequired

from project_todo.response import Response
from . import transformer
from .models import Users
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
   
@csrf_exempt
def auth(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        email = json_data['email']

        user = Users.objects.filter(email=email).first()

        if not user:
            return Response.notFound(message='User not found')

        if not check_password(json_data['password'], user.password):
            return Response.unauthorized(message="Email or password is incorrect")

        user = transformer.singleTransform(user)

        jwt = JWTAuth()
        user['token'] = jwt.encode({"id": user['id'], "email": user['email']})
        return Response.success(values=user, message="Login success")

@jwtRequired
@csrf_exempt
def index(request):
    if request.method == 'GET':
        user = Users.objects.all()
        user = transformer.transform(user)

        return Response.success(values=user)
    elif request.method == 'POST':
        json_data = json.loads(request.body)

        user = Users()
        user.name = json_data['name']
        user.email = json_data['email']
        user.password = make_password(password=json_data['password'])
        user.save()

        return Response.success(
            values=transformer.singleTransform(user), 
            message="User created",
        )
    else:
        return Response.badRequest(message="Invalid method")
        
@jwtRequired
@csrf_exempt
def show(request, id):
    user = Users.objects.filter(id=id).first()
    if not user:
        return Response.notFound(message="User not found")

    if request.method == 'GET':
        
        user = transformer.singleTransform(user)

        return Response.success(values=user)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)

        user.name = json_data['name']
        user.email = json_data['email']
        user.password = make_password(password=json_data['password'])
        user.save()

        return Response.success(
            values=transformer.singleTransform(user),
            message="User updated"
        )
    elif request.method == 'DELETE':
        user.delete()

        return Response.success(message="User deleted")
    else:
        return Response.badRequest(message="Invalid method")