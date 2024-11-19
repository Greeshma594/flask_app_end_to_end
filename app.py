from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/name')
def return_name():
    return "Hello from Greeshma"

@app.route('/ip')
def return_ip():
    hostname = socket.gethostname()
    get_ip = socket.gethostbyname(hostname)
    return get_ip
    

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=80 , debug=True)
