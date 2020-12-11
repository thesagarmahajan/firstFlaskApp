from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Motherfuckers!</h1>"

#  Send data using POST method and Selecting raw option in body tab of
#  Postman API Testing tool
@app.route("/postRawJson", methods=["POST"])
def postRawJson():
    return jsonify(request.json)

#  Send data using POST method and Selecting form-data option in body tab of
#  Postman API Testing tool
@app.route("/postFormData", methods=["POST"])
def postFormData():
    print(request.form.to_dict())
    return jsonify(request.form.to_dict())


#  Send data using POST method and Selecting x-www-form-urlencoded option in body tab of
#  Postman API Testing tool
@app.route("/x_www_form_urlencoded", methods=["POST"])
def x_www_form_urlencoded():
    print(request.form.to_dict())
    return jsonify(request.form.to_dict())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
