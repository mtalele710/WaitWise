from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to WaitWise!"

# 👇 THIS is the key part that runs the server
if __name__ == "__main__":
    app.run(debug=True)