from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<x>/<y>")
def checker_board(x,y):
    return render_template("checkerboard.html", x = int(x), y = int(y))

if __name__=="__main__":
    app.run(debug=True)