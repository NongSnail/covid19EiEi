from flask import Flask, render_template
import covid19

app = Flask(__name__)

@app.route('/')
def home():
    moew = {
        "Day" : covid19.upDate ,
        "sum" : covid19.cumulative ,
        "new" : covid19.new ,
        "severe" : covid19.severe ,
        "died" : covid19.died ,
        "refer" : covid19.refer ,
        "goHame" : covid19.goHome
    } 
    return render_template('myTemplate.html',**moew)



if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)