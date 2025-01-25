from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, CI/CD World!'

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye, CI/CD World!'

@app.route('/goodnight')
def goodbye_world():
    return 'goodnight'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
