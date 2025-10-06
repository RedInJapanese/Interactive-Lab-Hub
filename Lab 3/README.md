2# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

### Storyboard
Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

**Storyboard 1**
- Setting: A walkway. The handheld device uses a camera to view their surroundings. The user can ask the device where to go or what is in If they are approaching an obstacle or straying from a walkway, an auditory queue is played telling them where they need to go.
- Players: Blind individuals or persons with visual impairments. 
- Activity 1: when the user strays from the walkway.
<img width="1999" height="1520" alt="image" src="https://github.com/user-attachments/assets/ea1c4d87-2a34-437c-b96f-befc2c98fe36" />


**Storyboard 2**
- Setting: A walkway. The handheld device uses a camera to view their surroundings. The user can ask the device where to go or what is in If they are approaching an obstacle or straying from a walkway, an auditory queue is played telling them where they need to go.
- Players: Blind individuals or persons with visual impairments. 
- Activity 2: when the user approaches a fire hydrant.
<img width="2005" height="1383" alt="image" src="https://github.com/user-attachments/assets/a9cd9082-3331-47b3-988c-93ae799d85ff" />

**Storyboard 3**
- Setting: The user is stopped in the middle of nowhere. The handheld device uses a camera to view their surroundings. The user can ask the device where to go or what is in If they are approaching an obstacle or straying from a walkway, an auditory queue is played telling them where they need to go.
- Players: Blind individuals or persons with visual impairments. 
- Activity 3: when the user asks where they are.
<img width="1730" height="1187" alt="image" src="https://github.com/user-attachments/assets/cce453e7-ea3d-436f-9339-a3fe98ebe579" />

**Verplank Diagram**
<img width="3508" height="2480" alt="image" src="https://github.com/user-attachments/assets/7ef58650-4c72-48eb-b08b-576da705e4db" />


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

User: Where am I? 

Device: 11 East Loop Road, New York City

User: What is in front of me? 

Device: Fire hydrant

User approaches a fire hydrant 

Device: STOP! FIRE HYDRANT DETECTED!

User strays away from walkway

Device: STOP! DEVIATION DETECTED!



**Video Link: ** https://drive.google.com/file/d/1LquD3rQXZxGpD5Kh7e3VpPtcSlB84ukr/view?usp=sharing

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

The interaction wasn't all that different than what I thought. I will say that the person I was working with approached the chair a lot sooner than I thought. My original thought was to have the user go within 3-5 feet of an obstacle before the device sounded off. 

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
   - One thing that can change in my design is having the device let the user know that an object is X amount of meters away rather than immediately saying that it's close 
3. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
   - I'd also want to fully implement an image classifier so that it can recognize landmarks when navigating visually impaired individuals to their destinations
5. Make a new storyboard, diagram and/or script based on these reflections.
User: Where am I? 

Device: 11 East Loop Road, New York City

User: What is in front of me? 

Device: Fire hydrant

User approaches a fire hydrant 

Device: Fire hydrant 1 meter in front of you

User steps towards fire hydrant

Device: Fire hydrant 0.5 meters in front of you

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
  - using a proximity sensor
  - using the mic on the logitech webcam
* require participants to speak to it. 

*Document how the system works*
The system works by using a similar script to the `test_microphone.py` in which the user asks where they are. the device then uses socket code to get the public IP of where they are. Once they get the latitude and longitude of where you are, it then makes an API call to the geocoder library and gives your exact address. 
<img width="4032" height="3024" alt="image" src="https://github.com/user-attachments/assets/41b326a3-8832-46e0-8547-e57dd1dc78d2" />


*Include videos or screencaptures of both the system and the controller.*
**Interaction #1**
**Video 1: ** https://drive.google.com/file/d/1V6B-6HG_9P-10FRAyD1C0uKfSYjBXcfy/view?usp=sharing
**Video 2:** https://drive.google.com/file/d/1pKCFmXsvytORtMqWEy6nl3ywQfl_UIu3/view?usp=sharing
**Video 3:** https://drive.google.com/file/d/1RJB3I3uWRiQ-s9-oj_SS-bl7Ks29DLc_/view?usp=sharing

**Interaction #2**
**Video 4:** https://drive.google.com/file/d/1S9l_Zmyd5ti1ftXtvRXq6uhuxm7xA-4W/view?usp=sharing
**Video 5:** https://drive.google.com/file/d/1qEQdGE7uv7DAQd1owBYNyhQX-qAF_zP_/view?usp=sharing
**Video 6:** https://drive.google.com/file/d/1ZkmKDc6vyQJ4bzZ0orGvpVNRzPvJp62b/view?usp=sharing
<details>
  <summary><strong>Submission Cleanup Reminder (Click to Expand)</strong></summary>
  
  **Before submitting your README.md:**
  - This readme.md file has a lot of extra text for guidance.
  - Remove all instructional text and example prompts from this file.
  - You may either delete these sections or use the toggle/hide feature in VS Code to collapse them for a cleaner look.
  - Your final submission should be neat, focused on your own work, and easy to read for grading.
  
  This helps ensure your README.md is clear professional and uniquely yours!
</details>

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)
- Done
Answer the following:

### What worked well about the system and what didn't?
- What worked well is that the user was able to get where they are, but the problem is that sometimes this wouldn't work due to the server getting too many requests at a time.
### What worked well about the controller and what didn't?
\*\**your answer here*\*\*
- One thing that worked well is that the mic could pick up audio quite well even if you were 2 meters away. Howevern, you had to plug it into an outlet in order to use it. Additionally, the controller won't work if you leave the area with the wifi network it's using. This can be fixed with a power bank and hotspot, but at the time it was fairly inconvenient.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
\*\**your answer here*\*\*
- One thing I can take away is that the way you design a device will often times be very different from the way people will use it. Things that you thought were intuitive might not necessarily be the case for people actually trying to use the device. 

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*
- I could use an extra python script to take data from standard output and save it into a csv for me to analyze later. I can use the system to create a dataset by looking at specific things like how long it takes to detect objects, the distance at which it detects objects, how frequently failures happen when looking up location, etc.










