from flask import Flask, render_template

app = Flask("Mi primera página")

@app.route("/")
def index():
    return render_template("hola mundo.html")

if __name__=="__main__":
    app.run(debug=True)