from flask import Flask, jsonify, request
from datetime import datetime, timedelta


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def myendpoint():

    name = request.args.get('slack_name', 'Adeola19B')
    track = request.args.get('track', 'backend')
    file_url = "https://github.com/Adeola19B/hng/blob/main/app.py"
    repo_url = "https://github.com/Adeola19B/hng"
    
    now = datetime.utcnow()
    current = now.strftime('%A')
    utc = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    valid_time_range = now + timedelta(hours=-2), now + timedelta(hours=2)
    if ('since' in request.args) and ('until' in request.args):
        try:
            since = datetime.fromisoformat(request.args['since'])
            until = datetime.fromisoformat(request.args['until'])
        except ValueError:
            return jsonify({'error': 'Invalid Format'}), 400
        if (since < valid_time_range[0]) or (until > valid_time_range[1]):
            return jsonify({'error': 'Date of range range'}), 400

    
    data = {
        "slack_name": name,
        "current_day": current,
        "utc_time": utc,
        "track": track,
        "github_file_url": file_url,
        "github_repo_url": repo_url,
        "status_code": 200
    }
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')