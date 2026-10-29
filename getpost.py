from flask import Flask, render_template,request

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

@app.route("/form", methods=['GET','POST'])
def form():
    if request.method=='POST':
        # pass
        name=request.form['name']
        return f'hello{name}'
    return render_template('form.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        # pass
        name=request.form['name']
        return f'hello{name}'
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True) ### debug is used to update in localhost server without restarted it by user it automatically restart the server after just saving .py file in vs code 

 
