from flask import Flask, render_template, jsonify, request

# request 정보꺼내기,jsonify 제이슨형태로 뿌리기위해 사용.

app = Flask(__name__)


@app.route('/')  # 데코레이터
def hello_world():
    return render_template('server.html')  # rander_template >> html파일 가져오는거 ㅇㅇ


@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give') #?key = name & <질문하기
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
