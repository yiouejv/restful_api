from flask import Flask
from flask_restful import Api, Resource, reqparse, inputs
from config import session as db_session


app = Flask(__name__)

# 用api来绑定app
api = Api(app)


class LoginView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='用户名验证错误', required=True, trim=False)
        parser.add_argument('password', type=str, help='密码验证错误')
        parser.add_argument('age', type=int, help='年龄验证错误')
        parser.add_argument('gender', type=str, choices=['male', 'female'], help='性别验证错误')
        parser.add_argument('home_pager', type=inputs.url, help='个人中心链接验证错误')
        parser.add_argument('phone', type=inputs.regex(r'1[3578]\d{9}'), help='手机号码则是不正确', )
        parser.add_argument('brithday', type=inputs.date, help='生日验证错误', )
        args = parser.parse_args()
        print(args)
        return {"username": "yiouejv"}


api.add_resource(LoginView, '/login/', endpoint='login')

if __name__ == '__main__':
    app.run()
