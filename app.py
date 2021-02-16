from collections import OrderedDict
from datetime import datetime, timedelta

from flask import Flask

app = Flask(__name__)
store = OrderedDict()
ttl = {}
TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


def ttl_clear():
    now_time = datetime.utcnow()
    keys_to_delete = [key for key in ttl.keys() if datetime.strptime(ttl[key], TIME_FORMAT) <= now_time]
    for key in keys_to_delete:
        ttl.pop(key)
        store.pop(key)


@app.route('/GET/<key>', methods=["GET"])
def get_method(key):
    ttl_clear()
    value = store.get(key, None)
    return (value, 200) if value else ("Key doesn't exist.", 404)


@app.route('/KEYS/*', methods=["GET"])
def keys_method():
    ttl_clear()
    res = ''.join(f'{number+1}) "{key}"\n' for number, key in enumerate(store.keys()))
    return (res, 200) if res else ('', 404)


@app.route('/SET/<key>/<value>/PX=<int:px>/EX=<int:ex>', methods=["POST"])
@app.route('/SET/<key>/<value>/EX=<int:ex>/PX=<int:px>', methods=["POST"])
@app.route('/SET/<key>/<value>/PX=<int:px>', methods=["POST"])
@app.route('/SET/<key>/<value>/EX=<int:ex>', methods=["POST"])
@app.route('/SET/<key>/<value>', methods=["POST"])
def set_method(key, value, ex=0, px=0):
    ttl_clear()
    if ex or px:
        delta = {'seconds': ex, 'milliseconds': px}
        del_time = (datetime.utcnow() + timedelta(**delta)).strftime(TIME_FORMAT)
        ttl[key] = del_time
    store[key] = value
    return 'OK', 200


@app.route('/DEL/<key>', methods=["DELETE"])
def del_method(key):
    ttl_clear()
    if not store.get(key, None):
        return "Key doesn't exist.", 404
    del store[key]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
