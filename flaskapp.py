from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/uppercase',methods=['POST'])
def uppercase():
    data = request.get_json(force=True)
    text = data.get('text', '')
    result = text.upper()
    return jsonify({'result':result})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5002, debug = True)