from flask import Flask, render_template, make_response
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from config import session as db_session
from article_views import article_bp

app = Flask(__name__)
app.register_blueprint(article_bp)

api = Api(app)
# 返回html模板


@api.representation('text/html')
def output_html(data, code, headers):
    print(data)
    # 在representation装饰的函数中，必须返回一个Response对象
    resp = make_response(data)
    return resp


class ListView(Resource):
    def get(self):
        return render_template('list.html')


api.add_resource(ListView, '/list/', endpoint='list')


if __name__ == '__main__':
    app.run()
