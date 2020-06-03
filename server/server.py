import crawl
import database
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from requests.exceptions import ConnectionError

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route('/day', methods=['GET'])
def getDay():
    data = crawl.getDay()
    # print(data[1:])
    date = str(datetime.datetime.now().date())
    count = database.checkDateExists(date)
    if count == 0:
        database.insertWeathers(data[1:], date)
    return jsonify(data)


@app.route('/weather', methods=['GET'])
def getTomorow():
    try:
        if not request.args:
            return jsonify(crawl.getTomorow())
        else:
            seach = request.args['seach']
            return jsonify(database.findByDate(seach))
    except ConnectionError as e:
        print(e)
        return jsonify({'mesage': 'Not found!'})


@app.route('/days', methods=['GET'])
def getThreeDay():
    # url = ''
    try:
        number = request.args['number']
        return jsonify(
            crawl.getDays('http://www.thoitiethanoi.com/thoi-tiet-' + number + '-ngay-toi.html', int(number)))
    except Error as e:
        print(e)
    return jsonify({'mesage': 'Not found!'})


if __name__ == "__main__":
    app.run(host='localhost', port=4000, debug=False, threaded=False)
