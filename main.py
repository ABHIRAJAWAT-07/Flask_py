from flask import Flask, render_template

### WSGI application
app=Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to my  amazing and outstanding flask course. this is an amazing course"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True) ### debug is used to update in localhost server without restarted it by user it automatically restart the server after just saving .py file in vs code 

 
