from flask import Flask
from flask_restful import Api
from controllers.user_controller import user_blueprint

app = Flask(__name__)
api = Api(app)

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
