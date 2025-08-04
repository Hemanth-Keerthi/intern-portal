from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/intern', methods=['GET'])
def get_intern_data():
    return jsonify({
        "name": "Hemanth Keerthi",
        "referralCode": "hemanth2025",
        "donations": 9000
    })

if __name__ == '__main__':
    app.run(debug=True)
