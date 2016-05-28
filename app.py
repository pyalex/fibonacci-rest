import itertools
from flask import Flask, jsonify
app = Flask(__name__)

def fibonacci():
    n, m = 0, 1
    yield n
    yield m
    while True:
        yield n + m
        m, n = n + m, m

@app.route('/sequence/<limit>')
def endpoint(limit):
    try:
        limit = int(limit)
    except (TypeError, ValueError):
        return jsonify(error='N must be a non-negative integer'), 400

    if limit < 0:
        return jsonify(error='N must not be less than 0'), 400

    return jsonify(sequence=list(itertools.islice(fibonacci(), 0, limit)))


if __name__ == '__main__':
    app.run(debug=True)
