from flask import Flask
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from config import session as db_session
from article_views import article_bp

app = Flask(__name__)
app.register_blueprint(article_bp)


if __name__ == '__main__':
    app.run()
