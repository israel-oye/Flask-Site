from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

def dummy():
    4 + 5
    pass

if __name__ == "__main__":
    app.run()

