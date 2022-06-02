from flask import Flask, request, jsonify

app = Flask(__name__)

def test_api(param_1, param_2):
    return param_1+param_2

@app.route("/",methods=['GET','POST'])
def process():
    content = request.json

    result = {'result':test_api(content['pre'],content['suf'])}
    return jsonify(result)

if __name__ == '__main__':
    app.run('0.0.0.0',port=8080)