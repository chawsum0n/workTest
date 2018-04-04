from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Napier"

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested.",404

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world:("

if __name__ == "__main__":
    app.run()
