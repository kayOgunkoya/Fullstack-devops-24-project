from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Buster's Blog!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
