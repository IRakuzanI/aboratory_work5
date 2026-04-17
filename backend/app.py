import os
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def api_root():
    db_name = os.environ.get('DB_NAME', 'unknown')
    return jsonify({
        "status": "success",
        "message": "Backend успешно запущен",
        "database": db_name
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



