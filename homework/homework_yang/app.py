from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    su = request.form['su']
    address = request.form['address']
    phone = request.form['phone']

    print('name', name)
    print('su', su)
    print('address', address)
    print('phone', phone)
    # 여길 채워나가세요!

    # db에 정보 삽입하기.
    doc = {
        'name': name,
        'su': su,
        'address': address,
        'phone': phone
    }
    db.shoping.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문완료'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.shoping.find({}, {'_id': 0}))
    print(orders)
    # 여길 채워나가세요!
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
