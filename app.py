from flask import Flask, render_template, jsonify, request
import random, time
from database import init_db, insert_temp_humidity, get_temp_humidity_minutes, get_temp_humidity_history

app = Flask(__name__)

# Initialize DB on startup
init_db()

# ----------------------
# Routes
# ----------------------
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/act01_humidity_temp")
def temp_humidity():
    return render_template("act01_humidity_temp.html")

@app.route("/act02_distance")
def distance():
    return render_template("act02_distance.html")

@app.route("/act03_motion_sensor")
def motion_camera():
    return render_template("act03_motion_sensor.html")

@app.route("/act04_gas_vibration")
def gas_vibration():
    return render_template("act04_gas_vibration.html")

@app.route("/act05_sound_raindrop")
def sound_rain():
    return render_template("act05_sound_raindrop.html")

@app.route("/act06_gps")
def gps():
    return render_template("act06_gps.html")

@app.route("/act07_voice_led")
def voice_led():
    return render_template("act07_voice_led.html")

@app.route("/act08_tts")
def tts():
    return render_template("act08_tts.html")

@app.route("/act09_object_detection")
def object_detection():
    return render_template("act09_object_detection.html")

@app.route("/act10_face_recognition")
def face_recognition():
    return render_template("act10_face_recognition.html")

# ----------------------
# API Endpoints
# ----------------------

# Act01 - Temp & Humidity
@app.route('/get_temp_humidity')
def get_temp_humidity():
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)
    timestamp = int(time.time())

    # Save to DB
    insert_temp_humidity(timestamp, temperature, humidity)

    return jsonify({"temperature": temperature, "humidity": humidity, "timestamp": timestamp})

@app.route('/get_temp_humidity_minutes')
def get_minutes():
    return jsonify(get_temp_humidity_minutes())

@app.route('/get_temp_humidity_history')
def get_history():
    minute = request.args.get("minute")
    if not minute:
        return jsonify([])
    return jsonify(get_temp_humidity_history(minute))

# ----------------------
# Dummy Endpoints (Act02–Act10, no DB yet)
# ----------------------
@app.route("/get_distance")
def get_distance():
    return {"sensor1": random.randint(10, 200), "sensor2": random.randint(10, 200)}

@app.route("/get_motion")
def get_motion():
    return {"motion": random.choice([True, False])}

@app.route('/get_gas_vibration')
def get_gas_vibration():
    return {"gas": random.choice(["Safe", "Leak"]), "vibration": random.randint(0, 1)}

@app.route('/get_sound_rain')
def get_sound_rain():
    return {"sound": random.randint(30, 90), "rain": random.choice(["Dry", "Wet"])}

@app.route('/get_gps')
def get_gps():
    return {"lat": round(14.5995 + random.uniform(-0.01, 0.01), 5),
            "lng": round(120.9842 + random.uniform(-0.01, 0.01), 5)}

@app.route('/get_voice_led')
def get_voice_led():
    return {"command": random.choice(["ON", "OFF"]), "status": random.choice(["LED ON", "LED OFF"])}

@app.route('/get_tts')
def get_tts():
    return {"text": "Hello World", "status": "Played"}

@app.route('/get_object_detection')
def get_object_detection():
    return {"objects": random.choice([["Person"], ["Car"], ["Dog"], ["Cat"], ["None"]])}

@app.route('/get_face_recognition')
def get_face_recognition():
    return {"faces": random.randint(0, 3), "status": random.choice(["Recognized", "Unknown"])}

# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
