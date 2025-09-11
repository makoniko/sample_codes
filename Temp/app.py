from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/now", methods=["GET"])
def get_current_time():
    # 現在の時刻をISO 8601形式で返す
    now = datetime.now().isoformat()
    return jsonify({"now": now})

if __name__ == "__main__":
    app.run(debug=True)