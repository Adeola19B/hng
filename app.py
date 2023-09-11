from flask import Flask, jsonify
import datetime
app = Flask(__name__)

@app.route('/details', methods=['GET'])
def my_endpoint():
    data = {
        "slack_name": "Ehinmore Adeola Adebameno",
        "current_day": "Monday" ,
        "utc-time":datetime.datetime.today().isoformat(),
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