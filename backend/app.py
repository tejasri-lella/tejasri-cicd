from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student-details', methods=['GET'])
def student_details():
    return jsonify({
        "name": "Tejasri",
        "roll_number": "2023BCS0166"
    })

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)