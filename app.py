# flask import 하는 부분
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# pymongo import 하는 부분
from pymongo import MongoClient

# Certifi import 하는 부분 (Port 5000을 사용하기 위해서)
# import certifi
# ca = certifi.where()

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

    veggie_list = list(db.veggie.find({}, {'_id': False}))
    for veggie in veggie_list:
        if (title_receive != veggie.get('title')):
            title_2 = title_receive
        else:

            return jsonify({'msg': '그 야채는 이미 있습니다. 다른 녀석을 미워해주세요'})

    doc = {
        'image': url_receive,
        'comment': comment_receive,
        'title': title_2,
        'likes': 0
    }
    db.veggie.insert_one(doc)

    return jsonify({'msg': '불호의 역사를 새로 썼습니다!😎'})

@app.route("/veggie/likes", methods=["POST"])
def likes_post():
    title = request.form['title_give']
    veggie_list = list(db.veggie.find({}, {'_id': False}))
    for veggie in veggie_list:
        if (title == veggie.get('title')):
            likes = veggie.get('likes') + 1
            db.veggie.update_one({'title': title}, {'$set': {'likes': int(likes)}})

    return jsonify({'msg': '당신의 극혐에 투표 완료!'})


@app.route("/veggie", methods=["GET"])
def veggie_get():
    veggie_list = list(db.veggie.find({}, {'_id': False}).sort('likes', -1))
    return jsonify({'veggie': veggie_list})


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/broccoli')
def broccoli():
    return render_template('broccoli.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/comingsoon')
def comingsoon():
    return render_template('comingsoon.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)