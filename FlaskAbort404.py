from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Napier"

@app.route('/force404')
def force404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "Coudn't find the page you requested.",404

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world:("

if __name__ == "__main__":
    app.run()
