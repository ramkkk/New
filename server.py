import sys
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
_tput_ = 100

class ServerMain(Resource):
	def get(self):
		global _tput_
		_tput_ = _tput_ + 1
		print("+++++++++++++++++GET Method+++++++++++++")
		return _tput_

api.add_resource(ServerMain,"/TestServer")

if __name__ == '__main__':
   app.run(debug=True)
