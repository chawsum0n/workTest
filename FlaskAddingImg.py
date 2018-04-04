from flask import Flask,url_for
app = Flask(__name__)

@app.route("/")
def root():
    return "The default ,'root' route"

@app.route("/static-example/img")
def static_example_img():
    start = '<img src="'
    url = url_for('static',filename='IMG_3396.JPG')
    end = '">'
    return start+url+end,200

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world:("

if __name__ == "__main__":
    app.run()
