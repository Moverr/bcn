from flask import Flask,jsonify,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
   return  render_template('index.html')

@app.route('/registtration',method=['GET'])
def getRegistrations():
   return jsonify('Get all registration in the system')

@app.route('/registtration/<id>',method=['GET'])
def getRegistrationById(id):
   return jsonify('Registration by Id')


@app.route('/registtration',method=['POST'])
def register(id):
   return jsonify('Registration by Id')






@app.route('/profile/<profilename>')
def profile(profilename):
    return jsonify('profile.html', profile=profilename)





if __name__ == '__main__':
    app.run(debug=True)