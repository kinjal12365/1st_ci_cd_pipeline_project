from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=['GET'])

def welcome():
    return render_template("welcome.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=2000,debug=True)