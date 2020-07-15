import json
from flask import Flask,render_template, request, session, Response, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getIndex():
    return render_template('flow.html')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))

    # @app.route('/<data>', methods=['POST'])
    # def postData(data):
    #     c = json.loads(request.data)