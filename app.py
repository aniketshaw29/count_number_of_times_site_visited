from flask import Flask,render_template  #importinf flask

app = Flask(__name__) #magic variable main
#creating the Flask class object   

@app.route('/')     #decorator
def home():
    return render_template('home.html')

@app.route('/signup.html')     #decorator
def signup():
    return render_template('signup.html')

@app.route('/login.html')     #decorator
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
