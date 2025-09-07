from flask import Flask, render_template, jsonify, request
import random

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
@app.route('/temp_humidity')
def temp_humidity():
    return render_template("temp_humidity.html")

# =====================================================
# ACTIVITY 2: Distance Sensor + Buzzer
# =====================================================

distance_data = {"sensor1": "--", "sensor2": "--", "buzzer": "OFF"}

@app.route("/upload_distance", methods=["POST"])
def upload_distance():
    global distance_data
    data = request.get_json()

    # Get sensor data and convert to float if it's not empty
    sensor1 = data.get("sensor1")
    sensor2 = data.get("sensor2")

    # Only update the sensor data if valid
    if sensor1 is not None:
        distance_data["sensor1"] = float(sensor1)
    if sensor2 is not None:
        distance_data["sensor2"] = float(sensor2)

    # Automatically set buzzer status
    # If either sensor detects <= 12 cm, buzzer = ON
    if (sensor1 is not None and float(sensor1) <= 12) or (sensor2 is not None and float(sensor2) <= 12):
        distance_data["buzzer"] = "ON"
    else:
        distance_data["buzzer"] = "OFF"

    return jsonify({"status": "success"})

@app.route("/get_distance")
def get_distance():
    return jsonify(distance_data)

if __name__ == "__main__":
    app.run(debug=True)



@app.route('/motion_camera')
def motion_camera():
    return render_template("motion_camera.html")

@app.route('/gas_vibration')
def gas_vibration():
    return render_template("gas_vibration.html")

@app.route('/sound_rain')
def sound_rain():
    return render_template("sound_rain.html")

@app.route('/gps')
def gps():
    return render_template("gps.html")

@app.route('/voice_led')
def voice_led():
    return render_template("voice_led.html")

@app.route('/tts')
def tts():
    return render_template("tts.html")

@app.route('/object_detection')
def object_detection():
    return render_template("object_detection.html")

@app.route('/face_recognition')
def face_recognition():
    return render_template("face_recognition.html")


# ----------------------
# Example API Endpoints (dummy data for testing)
# Replace with real sensor logic later
# ----------------------
@app.route('/get_temp_humidity')
def get_temp_humidity():
    data = {
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 60), 2)
    }
    return jsonify(data)

@app.route('/get_distance')
def get_distance():
    data = {"distance": round(random.uniform(5, 100), 2)}
    return jsonify(data)

@app.route('/get_gas_vibration')
def get_gas_vibration():
    data = {"gas": random.choice(["Safe", "Leak"]), "vibration": random.randint(0, 1)}
    return jsonify(data)

@app.route('/get_sound_rain')
def get_sound_rain():
    data = {"sound": random.randint(30, 90), "rain": random.choice(["Dry", "Wet"])}
    return jsonify(data)

@app.route('/get_gps')
def get_gps():
    data = {"lat": 14.5995, "lng": 120.9842}  # Example: Manila
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)



# =====================================================
# ACTIVITY 1: Humidity & Temperature Sensor
# =====================================================
# temp_humid_data = {"temperature": "--", "humidity": "--"}
#
# @app.route("/upload_temp_humid", methods=["POST"])
# def upload_temp_humid():
#     global temp_humid_data
#     data = request.get_json()
#     temp_humid_data["temperature"] = data["temperature"]
#     temp_humid_data["humidity"] = data["humidity"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_temp_humid")
# def get_temp_humid():
#     return jsonify(temp_humid_data)

# =====================================================
# ACTIVITY 2: Distance Sensor
# =====================================================
# distance_data = {"distance": "--"}
#
# @app.route("/upload_distance", methods=["POST"])
# def upload_distance():
#     global distance_data
#     data = request.get_json()
#     distance_data["distance"] = data["distance"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_distance")
# def get_distance():
#     return jsonify(distance_data)

# =====================================================
# ACTIVITY 2: Distance Sensor + Buzzer
# =====================================================
# distance_data = {"sensor1": "--", "sensor2": "--", "buzzer": "OFF"}
#
# @app.route("/upload_distance", methods=["POST"])
# def upload_distance():
#     global distance_data
#     data = request.get_json()
#     distance_data["sensor1"] = data.get("sensor1")
#     distance_data["sensor2"] = data.get("sensor2")
#
#     # Automatically set buzzer status
#     # If either sensor detects <= 12 cm, buzzer = ON
#     if float(data.get("sensor1", 999)) <= 12 or float(data.get("sensor2", 999)) <= 12:
#         distance_data["buzzer"] = "ON"
#     else:
#         distance_data["buzzer"] = "OFF"
#
#     return jsonify({"status": "success"})
#
# @app.route("/get_distance")
# def get_distance():
#     return jsonify(distance_data)


# =====================================================
# ACTIVITY 3: Motion Sensor + Camera
# =====================================================
# motion_camera_data = {"motion": "--", "image_url": "--"}
#
# @app.route("/upload_motion_camera", methods=["POST"])
# def upload_motion_camera():
#     global motion_camera_data
#     data = request.get_json()
#     motion_camera_data["motion"] = data["motion"]
#     motion_camera_data["image_url"] = data["image_url"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_motion_camera")
# def get_motion_camera():
#     return jsonify(motion_camera_data)

# =====================================================
# ACTIVITY 4: Gas + Vibration Sensor
# =====================================================
# gas_vibration_data = {"gas": "--", "vibration": "--"}
#
# @app.route("/upload_gas_vibration", methods=["POST"])
# def upload_gas_vibration():
#     global gas_vibration_data
#     data = request.get_json()
#     gas_vibration_data["gas"] = data["gas"]
#     gas_vibration_data["vibration"] = data["vibration"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_gas_vibration")
# def get_gas_vibration():
#     return jsonify(gas_vibration_data)

# =====================================================
# ACTIVITY 5: Sound + Raindrop Sensor
# =====================================================
# sound_rain_data = {"sound": "--", "raindrop": "--"}
#
# @app.route("/upload_sound_rain", methods=["POST"])
# def upload_sound_rain():
#     global sound_rain_data
#     data = request.get_json()
#     sound_rain_data["sound"] = data["sound"]
#     sound_rain_data["raindrop"] = data["raindrop"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_sound_rain")
# def get_sound_rain():
#     return jsonify(sound_rain_data)

# =====================================================
# ACTIVITY 6: GPS Module
# =====================================================
# gps_data = {"latitude": "--", "longitude": "--"}
#
# @app.route("/upload_gps", methods=["POST"])
# def upload_gps():
#     global gps_data
#     data = request.get_json()
#     gps_data["latitude"] = data["latitude"]
#     gps_data["longitude"] = data["longitude"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_gps")
# def get_gps():
#     return jsonify(gps_data)

# =====================================================
# ACTIVITY 7: Voice Control LEDs
# =====================================================
# led_data = {"status": "--"}
#
# @app.route("/upload_led", methods=["POST"])
# def upload_led():
#     global led_data
#     data = request.get_json()
#     led_data["status"] = data["status"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_led")
# def get_led():
#     return jsonify(led_data)

# =====================================================
# ACTIVITY 8: Text-to-Speech
# =====================================================
# tts_data = {"text": "--", "audio_url": "--"}
#
# @app.route("/upload_tts", methods=["POST"])
# def upload_tts():
#     global tts_data
#     data = request.get_json()
#     tts_data["text"] = data["text"]
#     tts_data["audio_url"] = data["audio_url"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_tts")
# def get_tts():
#     return jsonify(tts_data)

# =====================================================
# ACTIVITY 9: Object Detection (Camera)
# =====================================================
# object_data = {"detected": "--", "image_url": "--"}
#
# @app.route("/upload_object", methods=["POST"])
# def upload_object():
#     global object_data
#     data = request.get_json()
#     object_data["detected"] = data["detected"]
#     object_data["image_url"] = data["image_url"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_object")
# def get_object():
#     return jsonify(object_data)

# =====================================================
# ACTIVITY 10: Face Recognition (Camera)
# =====================================================
# face_data = {"name": "--", "image_url": "--"}
#
# @app.route("/upload_face", methods=["POST"])
# def upload_face():
#     global face_data
#     data = request.get_json()
#     face_data["name"] = data["name"]
#     face_data["image_url"] = data["image_url"]
#     return jsonify({"status": "success"})
#
# @app.route("/get_face")
# def get_face():
#     return jsonify(face_data)
