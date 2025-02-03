from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Terraform Deployed Flask App!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
