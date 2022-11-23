from flask import Flask, render_template, request, redirect, url_for # we are importing the flask class from the flask module 

app = Flask(__name__) # this creates the application object

@app.route('/') # use the decoraders to link the functin to the url. are used to associate a URL to a function.then URL is associated with the home()function. so when the user requests that URL the view willrespond with a string.
def home():
    return "We made it " # returning a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST']) # specified the necessary HTTP methods for the route which are GET and POST, as arguments in the route decorator
def login():
    error = None
    if request.method == 'POST': # this is where the information come from
        if request.form['username'] != 'one' and request.form['password'] != 'one':
            error  = 'Wrong info. Try again!'
        else:
            return redirect(url_for('home')) # url_for gene4rates endpoint for provided method 
    return render_template('login.html', error=error)

if __name__ == '__main__':  # starting the server with 'run()' method 
    app.run(debug=True)


# after we import the Flask class, we create the application object, we define the view to respond to the requests, then start the server.