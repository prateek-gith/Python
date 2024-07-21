from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# it automatic Dedect The changement in File
app.run(debug=True)