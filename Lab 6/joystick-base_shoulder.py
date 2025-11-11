from __future__ import print_function
import qwiic_joystick
import time
import sys
import paho.mqtt.client as mqtt
import json

# --- MQTT Configuration ---
MQTT_BROKER = "farlab.infosci.cornell.edu"
MQTT_PORT = 1883
MQTT_TOPIC = "IDD/robotarm" 
MQTT_USER = "idd"
MQTT_PASSWORD = "device@theFarm"

# --- Servo Configuration ---
BASE_SERVO_MIN_ANGLE = 0
BASE_SERVO_MAX_ANGLE = 180
SHOULDER_SERVO_MIN_ANGLE = 70
SHOULDER_SERVO_MAX_ANGLE = 150

# --- Joystick Configuration ---
JOYSTICK_MIN = 0
JOYSTICK_MAX = 1023
JOYSTICK_CENTER = 512 # Assumes a 10-bit joystick (0-1023)
JOYSTICK_DEADZONE = 25 # +/- this value from center is treated as 0
SENSITIVITY = 0.5    # How fast the angle changes. Higher = faster.
LOOP_DELAY = 0.05    # Loop speed in seconds (20 Hz). Faster loop = smoother control.

# --- State Variables ---
# Store the current angle, starting at the middle position.
current_joint1_angle = (BASE_SERVO_MIN_ANGLE + BASE_SERVO_MAX_ANGLE) / 2
current_joint2_angle = (SHOULDER_SERVO_MIN_ANGLE + SHOULDER_SERVO_MAX_ANGLE) / 2

last_sent_joint1 = None
last_sent_joint2 = None
last_sent_button = None

# --- MQTT Setup ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker: {MQTT_BROKER}")
    else:
        print("Failed to connect, return code %d\n" % rc)

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
except AttributeError:
    print("Using legacy MQTT Client initialization.")
    client = mqtt.Client()

client.on_connect = on_connect

client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"Could not connect to MQTT broker: {e}", file=sys.stderr)
    sys.exit(1)

client.loop_start()

# --- Main Program Logic ---
def runExample():
    global current_joint1_angle, current_joint2_angle
    global last_sent_joint1, last_sent_joint2, last_sent_button

    myJoystick = qwiic_joystick.QwiicJoystick()

    if myJoystick.connected == False:
        print("The Qwiic Joystick device isn't connected...", file=sys.stderr)
        return

    myJoystick.begin()

    while True:
        # Read raw joystick values
        x_val = myJoystick.horizontal
        y_val = myJoystick.vertical
        button_val = myJoystick.button

        # 1. Calculate "speed" by subtracting the center
        # This gives a value from approx -512 to +512
        x_speed = x_val - JOYSTICK_CENTER
        y_speed = y_val - JOYSTICK_CENTER
        
        # 2. Apply the dead zone
        if abs(x_speed) < JOYSTICK_DEADZONE:
            x_speed = 0
        if abs(y_speed) < JOYSTICK_DEADZONE:
            y_speed = 0

        # 3. Calculate the change (delta) based on speed and sensitivity
        # Only calculate if x_speed/y_speed is not 0
        if x_speed != 0:
            delta_joint1 = x_speed * SENSITIVITY * LOOP_DELAY
            current_joint1_angle += delta_joint1

        if y_speed != 0:
            # Note: Y-axis might be inverted (0=up, 1023=down). 
            # If so, flip the sign: delta_joint2 = -y_speed * ...
            delta_joint2 = y_speed * SENSITIVITY * LOOP_DELAY * 0.25
            current_joint2_angle += delta_joint2
            
        # 4. Clamp the angles to stay within servo limits
        current_joint1_angle = max(BASE_SERVO_MIN_ANGLE, min(current_joint1_angle, BASE_SERVO_MAX_ANGLE))
        current_joint2_angle = max(SHOULDER_SERVO_MIN_ANGLE, min(current_joint2_angle, SHOULDER_SERVO_MAX_ANGLE))

        # Get the integer values for comparison
        int_joint1 = int(current_joint1_angle)
        int_joint2 = int(current_joint2_angle)
        
        if (int_joint1 != last_sent_joint1) or \
           (int_joint2 != last_sent_joint2) or \
           (button_val != last_sent_button):
            
            # 5. Create JSON payload
            payload_data = {
                "base": int_joint1,
                "shoulder": int_joint2,
                "button": button_val
            }
            json_payload = json.dumps(payload_data)
            
            # 6. Publish the message
            client.publish(MQTT_TOPIC, json_payload)

            # Move the print statement inside the 'if' block
            print(f"Sending: Base: {int_joint1}, Shoulder: {int_joint2}")

            # 7. --- NEW: Update the last sent state ---
            last_sent_joint1 = int_joint1
            last_sent_joint2 = int_joint2
            last_sent_button = button_val

        # Sleep for a short time
        time.sleep(LOOP_DELAY)

if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Program")
        client.loop_stop()
        client.disconnect()
        sys.exit(0)