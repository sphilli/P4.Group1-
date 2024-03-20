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
    sex_flag = int(content["sex_flag"])
    age = float(content["age"])
    fare = float(content["fare"])
    familySize = int(content["familySize"])
    p_class = int(content["p_class"])
    embarked = content["embarked"]

    preds = modelHelper.makePredictions(sex_flag, age, fare, familySize, p_class, embarked)
    return(jsonify({"ok": True, "prediction": str(preds)}))



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
