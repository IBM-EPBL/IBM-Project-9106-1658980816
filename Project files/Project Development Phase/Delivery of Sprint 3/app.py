#flask - it is used to run/serve application
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/web')
def web_load():
    return render_template('web.html')

if __name__=="__main__":
    app.run(debug=True)