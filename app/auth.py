# https://blog.teclado.com/learn-python-encrypting-passwords-python-flask-and-passlib/

import json
from flask import request, Blueprint, Response
from flask_restful import Api, Resource, reqparse, abort, fields
from flask import current_app as app
from os import environ

from .token import create_token
from .models import db, Users, user_schema, user_schema_with_pass
from .password import hash_password, verify_password

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['POST'])
def auth_login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    print(f'username: {username}  password: {password}')

    user_record = Users.query.filter_by(email=username).first()
    if not user_record:
        return "Forbidden", 401
    user = user_schema_with_pass.dump(user_record)

    if(verify_password(password, user['password'])):
        token = create_token(user)
        return {"token": token}
    else:
        return "Forbidden", 401

@auth.route('/signup', methods=['POST'])
def auth_signup():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    first_name = request.json.get('first_name', '')
    last_name = request.json.get('last_name', '')
    sign_up_code = request.json.get('sign_up_code', '')

    if(sign_up_code == environ.get('SIGN_UP_KEY') ):
        hashed_pass = hash_password(password)
        user = Users(email=username, password=hashed_pass, first_name=first_name, last_name=last_name)
        
        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)
        return result, 201
    else:
        return "Forbidden", 401




