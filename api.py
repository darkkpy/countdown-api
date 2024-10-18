from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/countdown', methods=['GET'])
def countdown():
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    target_date = ist.localize(datetime(now.year, 11, 1, 0, 0, 0))
    time_left = target_date - now

    days = time_left.days
    seconds_left = time_left.seconds
    hours = seconds_left // 3600
    minutes = (seconds_left % 3600) // 60
    seconds = seconds_left % 60
    milliseconds = time_left.microseconds // 1000

    return jsonify({
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'milliseconds': milliseconds
    })

if __name__ == '__main__':
    app.run(debug=True)
  
