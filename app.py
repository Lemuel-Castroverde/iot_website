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

@app.route("/get_distance")
def get_distance():
    # --- Random test values (active) ---
    return {
        "sensor1": random.randint(10, 200),
        "sensor2": random.randint(10, 200)
    }

# --- Real sensor code (commented for now) ---
    # dist1 = read_distance(TRIG1, ECHO1)
    # dist2 = read_distance(TRIG2, ECHO2)
    # return {"sensor1": dist1, "sensor2": dist2}

    

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
