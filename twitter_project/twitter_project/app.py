from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route("/twitter")
def index():
    return render_template("Home_page.html")

@app.route('/dunne', methods=['POST'])
def post_request():
    content = request.args.get("tweet", None, str)
    if content is None:
        return "Watch out for squidward", 400
    print(content)
    connection = psycopg2.connect(
                    user="postgres",
                    password="postgrespostgres",
                    host="localhost",
                    port="5432",
                    database="Practice data"
             )
    cursor = connection.cursor()

    insert_query = "INSERT INTO tweets (content) VALUES (%s); COMMIT;"
    cursor.execute(insert_query, (content,))
    

    return "Good Request", 200


if __name__ == '__main__':
    app.run(debug=True)
