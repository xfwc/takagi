from flask import Flask, g, jsonify,render_template, Response
from flask_cors import *
from flask_httpauth import HTTPBasicAuth
from flask import request
import re
import json

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dqzx2020@localhost:3306/takagi?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
CORS(app, resources=r'/*')
http_auth = HTTPBasicAuth()



def verify_password(username, password):
    result = Admin.login_or_not(username, password)
    return result

@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
#form表单
    # username = request.form['username']
    # password = request.form['password']
#param数据
    # username = request.args.get('username')
    # password = request.args.get('password')
    if request.json:
        phone = request.json.get('phoneNumber')
        password = request.json.get('password')
        result = Admin.login_or_not(phone, password)
        if result:
            return jsonify({'code': 200, 'msg': "登录成功", 'name': result})
        else:
            if None == result:
                return jsonify({'code': 404, 'msg': '无此用户,请确认手机号是否正确', 'name': None})
            return jsonify({'code': 404, 'msg': '密码错误，请检查密码是否正确', 'name': False})

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.json:
        username = request.json.get('username')
        password = request.json.get('password')
        phone = request.json.get('phone')
        result = Admin.register(username, password, phone)
        if result:
            return jsonify({'code': 200, 'msg': '注册成功'})
        return jsonify({'code': 500, 'msg': '这个手机号已经注册过啦'})


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
from .module import Admin