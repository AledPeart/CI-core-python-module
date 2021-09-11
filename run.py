import os
import json
from flask import Flask, render_template, request, flash  #imports the Flask class
if os.path.exists("env.py"):
    import env

app = Flask (__name__)   #creates an instance of the class Flask (capital letter denotes a class) and stores it in a vraiabe (app)  # uses a default python variable __name__ Flask needs this to find templates and static files
app.secret_key = os.environ.get("SECRET_KEY")                   


@app.route("/") #this is a function decorator. / is used so that when we browse to the root directory the functionality id triggered
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data) 
        for obj in data: 
            if obj["url"] == member_name:
                member = obj
    return  render_template("member.html", member=member) 


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
       flash("Thanks {}, we have received your message".format(request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

#the above is known a routing. connecting and rendering html content directly to a web page using flask


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("Port", "5000")),
        debug = True) #this allows us to see Python errors but should NEVR be used in a pridcution environment due to security reasons
    


