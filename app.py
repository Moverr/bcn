from flask import Flask,jsonify,render_template

app = Flask(__name__)

@app.route('/')
def index():
   return  render_template('index.html')

@app.route('/about')
def about():
   return jsonify('<h1> ABOUT US PAGE </h1>')


@app.route('/contact')
def contact():
   return jsonify('<h1> CONTACT US</h1>')

@app.route('/register')
def register():
   return jsonify('<h1> REGISTER</h1>')


@app.route('/profile/<profilename>')
def profile(profilename):
    return jsonify('profile.html', profile=profilename)





if __name__ == '__main__':
    app.run(debug=True)