from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("localhost", 27017)
db = client.dbsparta

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reviews", methods =["POST"])
def post_reviews():
    title_received = request.form["title"]
    author_received = request.form["author"]
    review_received = request.form["review"]

    review = {
        "title": title_received,
        "author": author_received,
        "review": review_received
    }

    db.reviews.insert_one(review)
    return jsonify({'result':'success', 'msg': '리뷰가 작성되었습니다'})

@app.route("/reviews", methods =["GET"])
def get_reviews():

    all_reviews = list(db.reviews.find({},{'_id':0}))
    return jsonify({"result": "success", 'msg': '리뷰를 받아왔습니다', 'reviews': all_reviews})

if __name__ == "__main__":
    app.run("localhost", port = 5000, debug = True)