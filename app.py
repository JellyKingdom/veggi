# flask import 하는 부분
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# pymongo import 하는 부분
from pymongo import MongoClient

# bs4 import 하는 부분
# from bs4 import BeautifulSoup

# Certifi import 하는 부분 (Port 5000을 사용하기 위해서)
import certifi

ca = certifi.where()

# request import 하는 부분
import requests

# MongoDB client, db 변수 선언
client = MongoClient('mongodb+srv://test:sparta@cluster0.urgl26q.mongodb.net/Cluster0@?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/veggie", methods=["POST"])
def veggie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    title_receive = request.form['title_give']
    likes_receive = request.form['likes_give']


    veggie_list = list(db.veggie.find({}, {'_id': False}))
    for veggie in veggie_list:
        if (title_receive != veggie.get('title')):
            title_2 = title_receive
        else:
            return jsonify({'msg': '중복입니다!'})




    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url_receive, headers=headers)

    # soup = BeautifulSoup(data.text, 'html.parser')

    # title = soup.select_one('meta[property="og:title"]')['content']
    # image = soup.select_one('meta[property="og:image"]')['content']

    doc = {
        'image': url_receive,
        'comment': comment_receive,
        'title': title_2,
        'likes': 0
    }
    db.veggie.insert_one(doc)

    return jsonify({'msg': '당신의 극혐에게 한 표를!😎'})


@app.route("/veggie/likes", methods=["POST"])
def likes_post():
    title = request.form['title_give']
    veggie_list = list(db.veggie.find({}, {'_id': False}))
    for veggie in veggie_list:
        if (title == veggie.get('title')):
            likes = veggie.get('likes') + 1
            db.veggie.update_one({'title': title}, {'$set': {'likes': int(likes)}})

    # print(likes)
    # db.veggie.update_one({'title': title}, {'$set': {'likes': int(likes)}})

    return jsonify({'msg': '투표완료?!'})



@app.route("/veggie", methods=["GET"])
def veggie_get():
    veggie_list = list(db.veggie.find({}, {'_id': False}))
    return jsonify({'veggie': veggie_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
