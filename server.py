from flask import Flask, request, render_template, flash, redirect, session, abort, jsonify
import pymsgbox
from Twitter import extracttweet
from models import Model
from depression_detection_tweets import DepressionDetection
from TweetModel import process_message
import os

app = Flask(__name__)


@app.route('/')
def root():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('main.html')
#edito main.html


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
        # pymsgbox.alert('This is an alert!')
        # pymsgbox.prompt('What is your name?')
        # return render_template("excep.html")
    return root()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return root()


@app.route("/sentiment")
def sentiment():
    return render_template("mentor.html")


# try1
@app.route("/test")
def test():
    return render_template("index.html")


@app.route("/main")
def home():
    return render_template("main.html")

@app.route("/textsenti")
def trule():
    return render_template("textsenti.html")

@app.route("/textsenti", methods=["POST"])
def predictSentiment():
    message = request.form['form10']
    pm = process_message(message)
    result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
    return render_template("tweetresult.html",result=result)


# global twitterUsername
# twitterUsername = 'narendramodi'


@app.route('/main', methods=["GET", "POST"])
def testAdil():
    # if request.method == "POST":
        # getting input with name = fname in HTML form
        twitterUsername = request.form.get("smid")
        if extracttweet(twitterUsername) == 404:
            flash('User Not Found:!')
            return render_template("excep.html")
        else :
            tweeto = extracttweet(twitterUsername)
            if (len(tweeto) == 0):
                flash('This User has no Tweets What we will analyse :')
                return render_template("excep.html")
            else:
                pm = process_message(tweeto)
                result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
                # return render_template("tweetresult.html", result=result)
                flash(tweeto)
                return render_template("tweetresult.html",result=result)
            return home()
        return home()

@app.route('/predict', methods=["POST"])
def predict():
    global result
    global opt_so
    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    if prediction[0] == 0:
        result = 'Your Depression test result : No Depression'
        opt_so = 'Suggestion : Congratulations ! You are Going Good , Be Cool. '
    if prediction[0] == 1:
        result = 'Your Depression test result : Mild Depression'
        opt_so = 'Optimal Solutions: Yoga, Excercise, Consult Psychatrist'
    if prediction[0] == 2:
        result = 'Your Depression test result : Moderate Depression'
        opt_so = 'Optimal Solutions: Pharmaco Therapy, Pills, Consult Psychatrist'
    if prediction[0] == 3:
        result = 'Your Depression test result : Moderately severe Depression'
        opt_so = 'Optimal Solutions: Yoga, Pills, Consult Psychatrist'
    if prediction[0] == 4:
        result = 'Your Depression test result : Severe Depression'
        opt_so = 'Optimal Solutions: Consult Psychatrist'
    return render_template("result.html", result=result, opt_so=opt_so)


app.secret_key = os.urandom(12)
app.run(host='localhost', port=8000, debug=True)
