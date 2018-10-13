from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
   return '<h1> HOME PAGE </h1>'

@app.route('/about')
def about():
   return '<h1> ABOUT US PAGE </h1>'


@app.route('/contact')
def contact():
   return '<h1> CONTACT US</h1>'

@app.route('/register')
def contact():
   return '<h1> REGISTER</h1>'




if __name__ == '__main__':
    app.run(debug=True)