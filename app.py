from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Bananas are great for small children!"    

@app.route("/html")
def html():
    return "<p>Bananas are great for small children!</p>"  

@app.route("/")
def monkey():
    return "monkey's will in turn eat small children"  
    
if __name__ == '__main__':
    app.run(use_reloader=True)

