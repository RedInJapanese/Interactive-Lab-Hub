# LAB 5, OBSERVANT SYSTEMS

**Collaborators:** Akash Basu, ab3334

---

## OVERVIEW:

In this lab, I created an **observant system** — an interactive Raspberry Pi device that can detect hands using media pipe and interpret them as ASL(American Sign Lagnauge) gestures.  
The goal was to explore how different “sense-making” algorithms (vision and ML models) can enable systems that recognize and react to what they see.  

My observant device uses **computer vision and neural networks** to detect gestures and trigger an action — similar to the "Boat Detector" to detect sign language. 

## TECHNICAL DESCRIPTION:

This is an application that utilizes mediapipe's landmark approach to tracking hands in order to train a neural network to recognize the sign language equivalent of letters of the alphabet. This is done by training a neural network using tensor flow that takes in 126 different landmark positions of the hand. Each letter in the sign language alphabets has 400 samples each, giving us a total of over 10,000 samples. The samples are taken using a script called `test.py` which takes the landmarks and saves each one as a `.npy` file. The next is `train.py` which uses tensor flow to train the model with 126 landmark positions. Lastly, I use `classify.py`, which takes probabilities based off landmark orientation of the live feed, the letter with the highest probability gets outputted and then I use the `pyttsx` library to give a voice output of the letter. The files that I used have been uploaded to the repository, but they have been zipped to save space.

<img width="2928" height="1592" alt="image" src="https://github.com/user-attachments/assets/b2ea920c-bab9-440b-9192-c243adef354d" />


**Landmarks are shown in the live video feed while the letter that it's reading is shown in the top left corner.**
---

## Part A — Play with Different Sense-Making Algorithms

### PYTORCH OBJECT RECOGNITION

I began by experimenting with **PyTorch’s MobileNet v2** model for real-time object recognition.  
After installing dependencies and connecting my webcam, I ran `infer.py`, which displayed the top object predictions from the live video feed.

**OBSERVATIONS:**
The model correctly recognized common objects like bottles, cups, and keyboards. The lighting and background strongly affected accuracy(I did not test this on objects with different colors, but I suspect that it would also have some sort of adverse effect on the model depending on both the color and background). Lastly, I noticed that the first few inferences were slower, but performance stabilized to around 30 fps after initialization.

**WHAT I LEARNED:**
Pretrained models can classify many object types, but they’re limited to the 1000 categories included in `classes.json`. Real-time inference on a Pi 4 is possible, but frame rate and latency can be an issue.

---

### MEDIAPIPE HAND AND POSE TRACKING

I explored **MediaPipe**, focusing on hand and pose detection.  
I used `hand_pose.py` and tested pinch detection** for continuous control (like a percentage slider) and quiet coyote gesture for discrete commands.

**OBSERVATIONS:**
I noticed that hand tracking was very robust in good lighting. Pinch detection worked best when the hand was near the center of the frame. Lastly, gestures could easily trigger events such as adjusting a servo, controlling brightness, or controlling the UI on my laptop.

**IDEA FOR INTERACTION:**
I propose using the gesture features of MediaPipe in order to detect ASL gestures. A tts package for python will be used to output the letters to audio. For tests, I will have new users attempt to spell their own names in ASL. 

---

### TEACHABLE MACHINES CUSTOM CLASSIFIER

I trained a model using **Google’s Teachable Machines** in order to test a more customizable approach. I made a basic image classifier to recognize:
1. **Hand up**  
2. **Hand down**  
3. **Background / nothing**

I collected ~50 samples per class, trained the model, and exported it as a TensorFlow Lite model (`.tflite` + `labels.txt`).  
After uploading it to the Pi, I ran `tml_example.py` to test live classification.

**OBSERVATIONS:**
The model worked well under normal lighting(room lighting, afternoon). It could distinguish between “hand up” and “hand down” pretty quickly. I also noticed it is more sensitive to background changes than MediaPipe.

**AFFORDANCES COMPARED TO OTHER METHODS:**
Unlike PyTorch, Teachable Machines allows training on *custom categories*. I also found it easier for rapid prototyping of specific recognition tasks. There is also a slightly slower and less robust than MediaPipe for motion-heavy inputs, but far simpler to deploy.

---

### SUMMARY OF ALGORITHM COMPARISOONS

| Tool | Input Type | Strengths | Weaknesses |
|------|-------------|------------|-------------|
| **PyTorch (MobileNet v2)** | Image classification | Pretrained, powerful, fast | Fixed 1000 classes |
| **MediaPipe** | Video (pose, face, hands) | Real-time, smooth tracking | Harder to customize categories |
| **Teachable Machines** | Image/audio | Easy to train custom models | Sensitive to lighting and camera setup |

---

## Part B — CONSTRUCT A SIMPLE INTERACTION

For my prototype, I used **MediaPipe hand tracking**.

### CONCEPT: "pose detection sign language" - using pose tracking to detect ASL gestures

The system landmark detection from Mediapipe to track the orientation of the hands for each letter of the alphabet. As mentioned above, `classify.py` is used in order to compare the live feed with the model generated from the training samples with the different ASL letters.

- **Input:** Hand gestures from a live feed.
- **Processing:** The system uses the probabilities from the model to see which letter the gesture is most likely to be .
- **Output:** The left hand corner will show the letter and also output it to standard output and TTS(text-to-speech).

**EXPERIMENTATION:**
Results vary depending on lighting. Because so many letters have similarities to one another, I had to invent gestures as replacements. Some gestures will overlap with one another due to similarity(eg.) 'h' and 'r' can be similar depending on the orientation). Very intuitive to control. Some letters are very difficult to obtain unless I spin the gesture itself around slightly. 

**VIDEO:**
- [Link](https://drive.google.com/file/d/19AzcspkMD5oyL5rGPes8NpyeTScMbbDv/view?usp=sharing)

**IMPROVEMENTS TO CONSIDER:**
- Use more landmarks to train the model with, will increase accuracy.
- Use a darker background to test the model with
- Maybe try testing with different skin tones?

---

## Part C — TEST THE INTERACTION

### OBSERVATIONS AND RESULTS

| Condition | Result | Notes |
|------------|---------|-------|
| Bright indoor light |  Accurate | MediaPipe detected hand easily |
| Similar signs for letters | Some misclassifications | Model lost hand landmarks for the letter 'r' |
| Darker background |  Slight Difficulty | Background motion confused detection |
| Hand partially off-screen | Failure | Detection dropped or jumped |

**WHEN IT WORKS:**  
When the hand is well-lit, centered, and within 50 cm of the camera.

**WHEN IT FAILS:**  
Low light, similar gestures, ambigious orientation.

**WHY IT FAILS:**  
MediaPipe relies on clear contour visibility. Poor lighting or motion blur causes landmark loss.

---

### THINKING FROM THE USER'S PERSPECTIVE

- **ARE THEY AWARE OF UNCERTAINTIES?**  
  Likely not — users may not understand why brightness flickers.
  
- **HOW BAD IS MISCLASSIFICATION?**  
  Not severe, but annoying(similar hand signs as mentioned prior) .

- **HOW TO ADDRESS IT?**
  Increase landmark threshold to 130 to increase accuracy
  
- **POSSIBLE OPTIMIZATIONS:**  
  - Lower camera resolution for faster FPS.  
  - Adjust MediaPipe confidence threshold.  
  - Implement temporal averaging for more stable output.

---

## Part D — Characterize the Observant System

**Material:** MediaPipe Hand Tracker

| Question | Answer |
|-----------|---------|
| What can you use it for? | Gesture-based controls (lights, motors, menus). |
| What is a good environment for it? | Well-lit, uncluttered backgrounds, steady camera. |
| What is a bad environment for it? | Dim or flickering light, complex motion backgrounds. |
| When will it break? | If there are similar hand signs, unclear hand orientation, or poor lighting. |
| How will it break? | Landmarks disappear; Similar model probabilities in `classify.py`. |
| Other properties/behaviors? | Smooth tracking when stable; easy to integrate with physical output devices. |
| How does it feel? | Bit of a learning curve if you don't know any ASL, apart from that it feels pretty natural  |

**VIDEO DEMO:**  
[Link](https://drive.google.com/file/d/1YkYun_KGj4wul5GSyCUNNDwun6d8GX-s/view?usp=sharing)
---

## SUMMARY

By experimenting with different sensing libraries, I developed an understanding of how computer vision tools differ in flexibility, robustness, and responsiveness.  
My prototype demonstrates how real-time hand tracking can be userd to interpret ASL and highlights challenges like lighting and stability.  

Next, I will refine and integrate the interaction into a final **observant system** and demonstrate it in use.

---

## Part 2 — FINAL INTERACTIVE SYSTEM

I've finished traning the model with a couple of hundred more samples from each letter, I have also attempted to introduce a space bar as a delimiter between letters so that participants can try to formulate actual sentences. Participants will also be looking at a chart containing the ASL letters for reference. 

NAME: Frank Xu 

**VIDEO:**
[Link](https://drive.google.com/file/d/1C19_zkD5Fxb9PHgtMHPaLVOfHrp1GsBx/view?usp=sharing)

**PLEASE NOTE THAT THE RASPBERRY PI IS BEING USED WITH THE GUI, BUT IT IS OUT OF FRAME IN THE VIDEO.**
