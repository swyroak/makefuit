from flask import Flask
from fruitname import fruitname

app = Flask(__name__)


@app.route('/')
def hello():

    return fruitname()


if __name__ == "__main__":
    app.run()
