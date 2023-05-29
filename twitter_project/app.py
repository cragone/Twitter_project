from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route("/twitter")
def index():
    return render_template("Home_page.html")

@app.route('/dunne', methods=['GET', 'POST'])
def post_request():
    if request.method == 'GET':
        return render_template("dunne.html")
    if request.method == 'POST':
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

            insert_query = "INSERT INTO tweets (id, content) VALUES (DEFAULT, %s)"
            cursor.execute(insert_query, (tweet,))

            connection.commit()
            cursor.close()
            connection.close()
            
            return "Tweet inserted successfully!"
        except (Exception, psycopg2.Error) as error:
            return f"Error: {error}"


if __name__ == '__main__':
    app.run(debug=True)
