<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from some_other_folder.some_other_class import Some_other_class


app = Flask(__name__)
db = SQLAlchemy()
    
@app.route("/")
def hello():
    return jsonify({"Status":"SUCCESS", "message":"Welcome to REST api with Flask"})
=======
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Motherfuckers!</h1>"
>>>>>>> cf668c8d186ea1a8f19673a2775be3434a57ff15

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

<<<<<<< HEAD

# This function returns the HTML template!
@app.route("/home_page")
def home_page():
    return render_template('pages/sampleInnerPage.html')

# Calling functions from user created python classes existing in different python files
@app.route("/moduleExample")
def moduleExample():
    ocObj = Some_other_class()
    return ocObj.sample_function1()

# Creating object dynamically of a class in different and call the class function requested from the url and pass parameters to the function 
# URL Format: /controller_name/function_name/param1/param2/...../param_n
# This function will update soon...stay tuned!!!

=======
>>>>>>> cf668c8d186ea1a8f19673a2775be3434a57ff15
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
