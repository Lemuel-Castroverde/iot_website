from flask import Flask, render_template, jsonify
import random, time

app = Flask(__name__)

# ----------------------
# Main Home Page
# ----------------------
@app.route('/')
def home():
    return render_template("index.html")

# ----------------------
# Activity Pages
# ----------------------
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
# Dummy API Endpoints
# ----------------------

# Act01 - Humidity & Temp (with history)
history_temp_hum = []
@app.route('/get_temp_humidity')
def get_temp_humidity():
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)
    timestamp = int(time.time())

    history_temp_hum.append({"time": timestamp, "temperature": temperature, "humidity": humidity})
    if len(history_temp_hum) > 50:
        history_temp_hum.pop(0)

    return jsonify({"temperature": temperature, "humidity": humidity})

@app.route('/get_temp_humidity_history')
def get_temp_humidity_history():
    return jsonify(history_temp_hum)


# Act02 - Distance
@app.route("/get_distance")
def get_distance():
    return {"sensor1": random.randint(10, 200), "sensor2": random.randint(10, 200)}


# Act03 - Motion Sensor (returns motion detected or not)
@app.route("/get_motion")
def get_motion():
    return {"motion": random.choice([True, False])}


# Act04 - Gas & Vibration
@app.route('/get_gas_vibration')
def get_gas_vibration():
    return {"gas": random.choice(["Safe", "Leak"]), "vibration": random.randint(0, 1)}


# Act05 - Sound & Rain
@app.route('/get_sound_rain')
def get_sound_rain():
    return {"sound": random.randint(30, 90), "rain": random.choice(["Dry", "Wet"])}


# Act06 - GPS
@app.route('/get_gps')
def get_gps():
    # Dummy Manila area (lat/lng changes slightly)
    return {"lat": round(14.5995 + random.uniform(-0.01, 0.01), 5),
            "lng": round(120.9842 + random.uniform(-0.01, 0.01), 5)}


# Act07 - Voice Controlled LED
@app.route('/get_voice_led')
def get_voice_led():
    return {"command": random.choice(["ON", "OFF"]), "status": random.choice(["LED ON", "LED OFF"])}


# Act08 - Text-to-Speech
@app.route('/get_tts')
def get_tts():
    return {"text": "Hello World", "status": "Played"}


# Act09 - Object Detection
@app.route('/get_object_detection')
def get_object_detection():
    return {"objects": random.choice([["Person"], ["Car"], ["Dog"], ["Cat"], ["None"]])}


# Act10 - Face Recognition
@app.route('/get_face_recognition')
def get_face_recognition():
    return {"faces": random.randint(0, 3), "status": random.choice(["Recognized", "Unknown"])}


# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
