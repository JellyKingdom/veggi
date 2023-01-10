from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.urgl26q.mongodb.net/Cluster0@?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/veggie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url_receive, headers=headers)

    # soup = BeautifulSoup(data.text, 'html.parser')

    # title = soup.select_one('meta[property="og:title"]')['content']
    # image = soup.select_one('meta[property="og:image"]')['content']
    if name

    doc = {
        'image':url_receive,
        'comment':comment_receive
    }

    db.veggie.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route("/veggie", methods=["GET"])
def veggie_get():
    veggie_list = list(db.veggie.find({}, {'_id': False}))
    return jsonify({'veggie':veggie_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)