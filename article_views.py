#encoding: utf-8

from flask import Blueprint
from flask_restful import Resource, fields, marshal_with, Api
from config import session as db_session
from models import Article

article_bp = Blueprint('article', __name__)

api = Api(article_bp)


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