from flask import Flask, render_template

from covid19 import ThaiPatient

app = Flask(__name__)

@app.route('/')
def home():
    patient =  {
        "thai" : ThaiPatient()
    } 
    return render_template('myTemplate.html',**patient["thai"])

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)