from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from some_other_folder.some_other_class import Some_other_class
from crud import crud


app = Flask(__name__)
db = SQLAlchemy()

# If none of th route gets match with the requested route from browser then this function will get execute
@app.errorhandler(404)
def not_found(e):
    return "URL Not Found"

# http://localhost:9090/ Hit this URL and it will trigger the following function
@app.route("/")
def hello():
    return jsonify({"Status":"SUCCESS", "message":"Welcome to REST api with Flask"})

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


# This function returns the HTML template!
@app.route("/home_page")
def home_page():
    return render_template('pages/sampleInnerPage.html')

# Calling functions from user created python classes existing in different python files
@app.route("/moduleExample")
def moduleExample():
    ocObj = Some_other_class()
    return ocObj.sample_function1()

# PostgreSQL Connection and CRUD Operations
# We cannot perform all CURD Operations in a single function. So let's create another python file and write a class in there!
@app.route('/crud/<fun>', methods=['GET', 'POST'])
@app.route("/crud/<fun>/<path:parameters>", methods=["GET", "POST"])
def requestHandler(fun, parameters="/"):
    crudObj = crud()
    if fun=="insert" and request.method=="POST":
        return crudObj.insert()
    elif fun=="list" and request.method=="GET":
        return crudObj.list()
    elif fun=="update" and request.method=="POST":
        return crudObj.update()
    elif fun=="delete" and request.method=="GET":
        return crudObj.delete()
    else:
        return "Invalid Operation or Method"
        
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
