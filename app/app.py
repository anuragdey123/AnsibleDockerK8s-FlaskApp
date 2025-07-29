from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to My Flask App — Deployed on Kubernetes using Ansible & Docker by Anurag "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
