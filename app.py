from flask import Flask, jsonify
from datetime import datetime


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def myendpoint():
    now = datetime.utcnow()
    current = now.strftime('%A')
    utc = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    valid_time_range = now + timedelta(hours=-2), now + timedelta(hours=2)
    if ('since' in request.args) and ('until' in request.args):
        try:
            since = datetime.fromisoformat(request.args['since'])
            until = datetime.fromisoformat(request.args['until'])
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), 400
        if (since < valid_time_range[0]) or (until > valid_time_range[1]):
            return jsonify({'error': 'Date range is out of valid time range'}), 400

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