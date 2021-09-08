import os
from flask import Flask, render_template  #imports the Flask class

app = Flask (__name__) #creates an instance of the class Flask (capital letter denotes a class) and stores it in a vraiabe (app)
                        # uses a default python variable __name__ Flask needs this to find templates and static files

@app.route("/") #this is a function decorator. / is used so that when we browse to the root directory the functionality id triggered
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

#the above is known a routing. connecting and rendering html content directly to a web page using flask


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("Port", "5000")),
        debug = True) #this allows us to see Python errors but should NEVR be used in a pridcution environment due to security reasons
    


