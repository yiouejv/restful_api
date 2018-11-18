from flask import Flask
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from config import session as db_session
from models import *


app = Flask(__name__)

# 用api来绑定app
api = Api(app)


# class ArticleView(Resource):
#     resource_fields = {
#         'title': fields.String,
#         'content': fields.String
#     }
#
#     # restful规范中，要求，定义好了返回的参数
#     # 即使这个参数没有值，也应该返回值， 返回一个None
#
#     @marshal_with(resource_fields)
#     def get(self):
#         return {'title': 'xxx'}
#
#
# api.add_resource(ArticleView, '/article/', endpoint='article')


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


# 定义一个flask_restful_api的视图
class ArticleView(Resource):
    resource_fields = {
        'article_title': fields.String(attribute='title'),  # 重命名属性
        'content': fields.String,
        'author': fields.Nested({
            'username': fields.String,
            'email': fields.String,
        }),
        'tags': fields.List(fields.Nested({
            'id': fields.Integer,
            'name': fields.String,
        })),
        'read_count': fields.Integer(default=80),  # 设置默认值
    }

    @marshal_with(resource_fields)
    def get(self, article_id):
        article = db_session.query(Article).filter(Article.id==article_id).first()
        return article


api.add_resource(ArticleView, '/article/<int:article_id>/', endpoint='article')


@app.route('/')
def index():
    user = User(username='xxx', email='xxx@126.com')
    article = Article(title='abc', content='123')
    article.author = user
    tag1 = Tag(name='前端')
    tag2 = Tag(name='python')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db_session.add(article)
    db_session.commit()
    return 'ok'


if __name__ == '__main__':
    app.run()
