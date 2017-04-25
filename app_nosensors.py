
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

# Data Inquirer main page
@app.route('/data_inquirer')
def index_di():
    return render_template('index_data_inquirer.html')

# Daily data main page
@app.route('/daily_data')
def index_dd():
    return render_template('index_daily_data.html')

@app.route('/cameras_immigrants.html')
def cameras_immigrants():
    return render_template('cameras_immigrants.html')


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)