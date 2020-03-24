from flask import Flask, render_template

from covid19 import patient

app = Flask(__name__)

@app.route('/')
def home():
    moew = {
        "Day" : patient["update"]() ,
        "sum" : patient["cumulative"]() ,
        "new" : patient["new"]() ,
        "severe" : patient["severe"]() ,
        "died" : patient["dead"]() ,
        "refer" : patient["references"]() ,
        "goHome" : patient["goHome"]()
    } 
    return render_template('myTemplate.html',**moew)



if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)