
from flask import render_template, Flask, jsonify, request
import sensor_data  #~ for testing purposes
import microphone_level
import force
# I may not need the request here since I'm not getting user input
app = Flask(__name__)
inp = microphone_level.setup()   #~Set up audio input from USB microphone
force.setup()					 #~Set up GPIO pin for force input


#~ I may need to put this somewhere else..not sure if it executes without being called below
@app.before_first_request
#can put function here to run prox. sensor files
def on_boot():
	pass


#~ Get sound data from microphone
@app.route('/_get_sound')
def get_sound_func():
    sound = microphone_level.get_sound(inp)
    return jsonify(result=sound)
    
#~ Get force data from mat
@app.route('/_get_force')
def get_force():
    force_val = force.get_force_read()
    return jsonify(result=force_val)

#~ Get force and sound randomized data for testing
@app.route('/_get_time')
def get_time():
    sensorData = sensor_data.run()
    return jsonify(result=sensorData)

# Data Inquirer main page
@app.route('/data_inquirer')
def index_di():
    return render_template('index_data_inquirer.html')

# Daily data main page
@app.route('/daily_data')
def index_dd():
    return render_template('index_daily_data.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)
