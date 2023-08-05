from flask import Flask
from flask_restful import Api
from controllers.user_controller import UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/users', '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
