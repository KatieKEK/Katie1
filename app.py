from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Bananas are great for small children!"    

@app.route("/html")
def html():
    return "<p>Bananas are great for small children!</p>"  

@app.route("/monkeys")
def monkey():
    return "monkeys will in turn eat small children"  
    
if __name__ == '__main__':
    app.run(use_reloader=True)

