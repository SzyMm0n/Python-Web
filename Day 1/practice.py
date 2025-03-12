from flask import Flask,url_for,render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index_page():
    #Rendering my template
    return  render_template('index.html')

@app.route('/hello/')
def hello(name =  '<script>alert("bad")</script>'):
    #Without 'escape' script causing alert is executed
    return escape(f"<h1>Hello {name}!</h1>")


if __name__ == "__main__":
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )