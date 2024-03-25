from flask import Flask, request, Response
from flask_cors import CORS

import os
from src.controllers.llm.chat import (main as chat)

app = Flask(__name__)
CORS(app)

directory = os.path.dirname(__file__) + "/utils"
filename = "pineconeConnection.py"

# Join the directory and filename to create the file path
file_path = os.path.join(directory, filename)

exec(open(file_path).read())

@app.route("/")
def hello_world():
    return Response("{'a':'b'}", status=200, mimetype='application/json')


@app.route("/chat", methods=['POST'])
def controller():
    try:
        body = request.json
        return chat(Response, body)
    except Exception as e:
        return {
            'status': 'failed',
            'message': str(e)
        }
