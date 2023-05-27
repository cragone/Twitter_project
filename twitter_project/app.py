from flask import Flask, render_template, request, flash
import psycopg2

app = Flask(__name__)

@app.route("/twitter")
def index():
    return render_template("Home_page.html")

@app.route('/dunne', methods=['GET','POST'])
def post_request():
    if request.method == 'GET':
        return "This is a GET request."
    if request.method == 'POST':
        tweet_number = request.form.get('number')
        tweet = request.form.get('content')


try:
            connection = psycopg2.connect(
                user="postgres",
                password="postgrespostgres",
                host="localhost",
                port="5432",
                database="Practice data"
            )

            cursor = connection.cursor()


if __name__ == '__main__':
    app.run(debug=True)