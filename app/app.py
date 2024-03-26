from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper
import json

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()



@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/ml_live_form")
def ml_live_form():
    return render_template("ml_live_form.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/tableau")
def tableau():
    return render_template("tableau.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    gender = int(content["gender"])
    own_car = int(content["own_car"])
    own_property = int(content["own_property"])
    unemployed = int(content["unemployed"])
    family_status = content["family_status"]
    education_type = content["education_type"]
    housing_type = content["housing_type"]
    income_type = content["income_type"]
    occupation_type = content["occupation_type"]
    age = float(content["age"])
    num_children = int(content["num_children"])
    num_family = int(content["num_family"])
    account_length = int(content["account_length"])
    total_income = float(content["total_income"])
    years_employed = float(content["years_employed"])


    preds = modelHelper.makePredictions(gender, own_car, own_property, unemployed, num_children,
                       num_family, account_length, total_income, age, years_employed, income_type, 
                        education_type, family_status, housing_type, occupation_type)
    return(jsonify({"ok": True, "prediction": preds}))



#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
