from flask import Flask, render_template
# render_template It  Is Use To Templet Which Is Created In Templet Folder

app = Flask(__name__)

# this is end point It mean When We Run Our Site In The server Or Local Server Then We 
# Use '/' It Mean Fornt Page 
# Like This We Creat End Point
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/prateek")
def Hello_Prateek():
    return "<p>Hellow Prateek Bhai</p>"

# it automatic Dedect The changement in File
app.run(debug=True)