from flask import Flask, render_template, jsonify
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

@app.route('/distance')
def distance():
    return render_template("distance.html")

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
