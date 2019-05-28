from flask import Flask
app = Flask(__name__)
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')


@app.route("/")
def index():
    return "Bananas are great for small children!"    

@app.route("/images/Liptak_Agent_Picture.png")
def Liptak_Agent_Picture():
    return send_from_directory(static_file_dir, 'Liptak_Agent_Picture.png')

@app.route("/images/eye_icon.ico")
def icon():
    return send_from_directory(static_file_dir, 'eye_icon.ico')

@app.route("/images/Liptak_Agent_Picture.png")
def Liptak_Agent_Picture():
    return send_from_directory(static_file_dir, 'Liptak_Agent_Picture.png')

@app.route("/monkeys")
def monkey():
    return "monkeys will in turn eat small children"  
    
if __name__ == '__main__':
    app.run(use_reloader=True)

