from flask import Flask

app = Flask(__name__)


@app.route('/wechat_api')
def test():
    return "test for wechat pub~"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
