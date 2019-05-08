from flask import Flask
from flask import render_template
from flask import request
from fruitname import fruitname
from fruitname import realfruit

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('main.html', name='ボタンを押すとみの名前が出るよ')


@app.route('/test', methods=['POST', 'GET'])
def test():
    name = fruitname()
    flg = realfruit(name)
    return render_template('main.html', name=name, flg=flg)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run('0.0.0.0',port=8080)
