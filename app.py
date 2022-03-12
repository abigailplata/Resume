from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',my_name='Abigail Plata')

@app.route('/resume', methods=['GET','POST'])
def resume():
    if request.method == 'POST':
        # can do stuff when the form is submitted
        #redirect to end the POST handling
        #the redirect can be to the same route or elsewhere
        return redirect(url_for('index'))
    #show the form, it wasnt submitted
    return render_template('resume.html')