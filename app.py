from flask import Flask, jsonify
from datetime import datetime


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def myendpoint():
    now = datetime.utcnow()
    current = now.strftime('%A')
    utc = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    data = {
        "slack_name": "Adeola19B",
        "current_day": current,
        "utc-time":utc,
        "track": "backend",
        "github_file_url": "https://github.com/Adeola19B/hng/blob/main/app.py",
        "github_repo_url": "https://github.com/Adeola19B/hng",
        "status_code": 200
    }
    response = jsonify(data)

    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == "__main__":
    app.run()