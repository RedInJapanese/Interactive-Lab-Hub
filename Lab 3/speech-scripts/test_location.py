#!/usr/bin/env -S /home/pi/Interactive-Lab-Hub/Lab\ 3/.venv/bin/python


# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import argparse
import queue
import sys
import sounddevice as sd
import json

from vosk import Model, KaldiRecognizer
import requests
import socket
from geopy.geocoders import Nominatim
import subprocess
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from opencage.geocoder import OpenCageGeocode

q = queue.Queue()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l", "--list-devices", action="store_true",
    help="show list of audio devices and exit")
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-f", "--filename", type=str, metavar="FILENAME",
    help="audio file to store recording to")
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
parser.add_argument(
    "-r", "--samplerate", type=int, help="sampling rate")
parser.add_argument(
    "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
args = parser.parse_args(remaining)


voice = ""

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])
        
    if args.model is None:
        model = Model(lang="en-us")
    else:
        model = Model(lang=args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
            dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                print("Final:", result.get("text", ""))
                voice = result.get("text", "")
                if voice == "where am i":
                    public_ip = "8.8.8.8"
                    try:
                        response = requests.get("https://api.ipify.org")
                        public_ip = response.text
                        print(f"Your public IP address is: {public_ip}")
                    except requests.exceptions.RequestException as e:
                        print(f"Error getting public IP: {e}")
                    try:
                        response = requests.get("https://ipapi.co/" + public_ip + "/json/")
                        data = response.json()
                        print(data)
                        print(f"City: {data.get('city')}")
                        print(f"Region: {data.get('region')}")
                        print(f"Country: {data.get('country_name')}")
                        print(f"Latitude: {data.get('latitude')}")
                        print(f"Longitude: {data.get('longitude')}")

                        geolocator = Nominatim(user_agent="my_app")
                        # Replace with your obtained latitude and longitude
                        lat_long = ""
                        lat_long =  "" + str(data.get('latitude')) + ", " + str(data.get('longitude'))
                        print(lat_long)
                        geolocator = Nominatim(user_agent="my_app_name")   # set a descriptive user_agent
                        reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)  # polite: 1s between requests

                        lat, lon = data.get('latitude'), data.get('longitude')
                        if lat is not None and lon is not None:
                            API_KEY = "2270f1fcc4e1446ebbb6fc6ff597ac0d"
                            geocoder = OpenCageGeocode(API_KEY)
                            location = geocoder.reverse_geocode(lat, lon)                            
                            if location:
                                print(location[0]['formatted'])
                                command = "echo " + f'"You are currently in: {location[0]}"' + " | festival --tts"
                                subprocess.Popen(command, shell=True)
                            else:
                                print("No result")
                        else:
                            lat, lon = 40.7621, -73.9517
                            API_KEY = "2270f1fcc4e1446ebbb6fc6ff597ac0d"
                            geocoder = OpenCageGeocode(API_KEY)
                            location = geocoder.reverse_geocode(lat, lon)                            
                            if location:
                                print(location[0]['formatted'])
                                command = "echo " + "You are currently in: " +location[0]['formatted'] + " | festival --tts"
                                subprocess.Popen(command, shell=True)
                            else:
                                print("No result")

                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching IP geolocation: {e}")
                elif voice == "what is in front of me":
                    command = "echo " + "Nothing is in front of you" + " | festival --tts"
                    subprocess.Popen(command, shell=True)
            else:
                print(rec.PartialResult())

except KeyboardInterrupt:
    print("\nDone")
    print(voice)
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))
