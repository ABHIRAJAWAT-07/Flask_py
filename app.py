from flask import Flask

### WSGI application
app=Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to my  amazing and outstanding flask course. this is an amazing course"

@app.route("/index")
def index():
    return "hello buddy Rajawat is speaking"


if __name__=="__main__":
    app.run(debug=True) ### debug is used to update in localhost server without restarted it by user it automatically restart the server after just saving .py file in vs code 

 
