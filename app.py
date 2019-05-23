from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Bananas are great for small children!"    
    
if __name__ == '__main__':
    app.run(use_reloader=True)

