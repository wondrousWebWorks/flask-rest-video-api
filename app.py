from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "johann":
        {
            "nationality": "South African",
            "age": 38
        },
    "carlos":
        {
            "nationality": "Spanish",
            "age": 39
        }
}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
