
from flask import render_template, Flask, jsonify, request
import sensor_data
# I may not need the request here since I'm not getting user input
app = Flask(__name__)

@app.route('/_get_time')
def get_time():
    sensorData = sensor_data.run()
    return jsonify(result=sensorData)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = False
    app.run(host='192.168.1.48', port=5010)