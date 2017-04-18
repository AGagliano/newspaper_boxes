
from flask import render_template, Flask, jsonify, request
import alsaaudio
import sensor_data
import microphone_level
# I may not need the request here since I'm not getting user input
app = Flask(__name__)

#~ I may need to put this somewhere else..not sure if it executes without being called below
@app.before_first_request
def test_print():
	print("ran this before starting website")


#~ Get sound data from microphone
@app.route('/_get_time')
def get_time():
    sensorData = sensor_data.run()
    return jsonify(result=sensorData)

#~ Get force and sound randomized data for testing
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
