from flask import Flask, request, jsonify
from dotenv import load_dotenv
import psycopg2
from datetime import datetime


app = Flask(__name__)
load_dotenv()

conn = psycopg2.connect(host="localhost", user="postgres", password="1998", dbname="snakegame_db")

INSERT_USER = ("INSERT INTO score (user_name, score, date) VALUES (%s, %s, %s);")
GET_ALL_SCORES = ("SELECT * FROM score;")
GET_TOP_TEN = ("SELECT user_name,score FROM score ORDER BY score DESC LIMIT 10;")

@app.get("/get_all_scores")
def get_all_scores():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_ALL_SCORES)
            res = cursor.fetchall()
    return jsonify(res)

@app.post("/user_score")
def post():
    data = request.get_json()
    user_name = data["user_name"]
    score = data["score"]
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(INSERT_USER, (user_name, score, date))
    return {"message": "User added."}, 201

@app.get("/top_ten_scores")
def get_top_ten():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_TOP_TEN)
            res = cursor.fetchall()
    return jsonify(res)




