# Observant Systems

**Collaborators:** Akash Basu, ab3334

---

## Overview

In this lab, I created an **observant system** — an interactive Raspberry Pi device that can detect and respond to events in its environment.  
The goal was to explore how different “sense-making” algorithms (vision and ML models) can enable systems that recognize and react to what they see.  

My observant device uses **computer vision and machine learning** to detect motion, gestures, or specific objects, and trigger an action — similar to the "Boat Detector" to detect sign language  

---

## Part A — Play with Different Sense-Making Algorithms

### PyTorch Object Recognition (MobileNet v2)

I began by experimenting with **PyTorch’s MobileNet v2** model for real-time object recognition.  
After installing dependencies and connecting my webcam, I ran `infer.py`, which displayed the top object predictions from the live video feed.

**Observations:**
- The model correctly recognized common objects like bottles, cups, and keyboards.  
- Lighting and background strongly affected accuracy.  
- The first few inferences were slower, but performance stabilized to around 30 fps after initialization.

**What I learned:**
- Pretrained models can classify many object types, but they’re limited to the 1000 categories included in `classes.json`.
- Real-time inference on a Pi 4 is possible, but frame rate and latency can be an issue.

---

### MediaPipe Hand and Pose Tracking

I explored **MediaPipe**, focusing on hand and pose detection.  
I used `hand_pose.py` and tested pinch detection** for continuous control (like a percentage slider) and quiet coyote gesture for discrete commands.

**Observations:**
- Hand tracking was very robust in good lighting.
- Pinch detection worked best when the hand was near the center of the frame.
- Gestures could easily trigger events such as adjusting a servo or controlling brightness.

**Idea for interaction:**
I considered using MediaPipe’s pinch percentage to control a servo motor or LED brightness — effectively using your hand as a “virtual knob” in the air.

---

###Teachable Machines Custom Classifier

To test a more customizable approach, I trained a model using **Google’s Teachable Machines**.  
I built a simple image classifier to recognize:
1. **Hand up**  
2. **Hand down**  
3. **Background / nothing**

I collected ~20 samples per class, trained the model, and exported it as a TensorFlow Lite model (`.tflite` + `labels.txt`).  
After uploading it to the Pi, I ran `tml_example.py` to test live classification.

**Observations:**
- The model worked well under normal lighting(room lighting, afternoon).
- distinguished between “hand up” and “hand down” pretty quickly.
- More sensitive to background changes than MediaPipe.

**Affordances compared to other methods:**
- Unlike PyTorch, Teachable Machines allows training on *custom categories*.
- Easier for rapid prototyping of specific recognition tasks.
- Slightly slower and less robust than MediaPipe for motion-heavy inputs, but far simpler to deploy.

---

### Summary of Algorithm Comparisons

| Tool | Input Type | Strengths | Weaknesses |
|------|-------------|------------|-------------|
| **PyTorch (MobileNet v2)** | Image classification | Pretrained, powerful, fast | Fixed 1000 classes |
| **MediaPipe** | Video (pose, face, hands) | Real-time, smooth tracking | Harder to customize categories |
| **Teachable Machines** | Image/audio | Easy to train custom models | Sensitive to lighting and camera setup |

---

## Part B — Construct a Simple Interaction

For my prototype, I used **MediaPipe hand tracking**.

### Concept: “Air Dimmer” — Hand-Controlled Light Brightness

The system uses **pinch distance** from MediaPipe to control the brightness of an LED connected to the Raspberry Pi.

- **Input:** Hand pinch percentage detected from the webcam feed.
- **Processing:** The system maps pinch distance (0–1) to LED brightness (0–255 PWM).
- **Output:** The LED dims or brightens in real time as you pinch and release.

**Experimentation:**
- Works well under stable lighting.
- Very intuitive to control — feels like turning a virtual knob in midair.
- Pinch percentage occasionally jumped when the hand was partially out of frame, causing flicker.

**Improvements to consider:**
- Apply smoothing or hysteresis to stabilize LED brightness.
- Add visual feedback (e.g., on-screen bar) to show brightness level.

---

## Part C — Test the Interaction Prototype

### Observations and Results

| Condition | Result | Notes |
|------------|---------|-------|
| Bright indoor light |  Accurate | MediaPipe detected hand easily |
| Dim lighting | Some misclassifications | Model lost hand landmarks |
| Moving background | Flicker | Background motion confused detection |
| Hand partially off-screen | Failure | Detection dropped or jumped |

**When it works:**  
When the hand is well-lit, centered, and within 50 cm of the camera.

**When it fails:**  
Low light, partial occlusion, or fast hand movements.

**Why it fails:**  
MediaPipe relies on clear contour visibility. Poor lighting or motion blur causes landmark loss.

---

### Thinking from the User’s Perspective

- **Are they aware of uncertainties?**  
  Likely not — users may not understand why brightness flickers.
  
- **How bad is a misclassification?**  
  Not severe (LED flickers), but annoying.

- **How to address it?**  
  Add smoothing filters or display feedback (like “hand not detected” message).

- **Possible optimizations:**  
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
| When will it break? | If the hand moves too fast, or exits the frame. |
| How will it break? | Landmarks disappear; output jumps or freezes. |
| Other properties/behaviors? | Smooth tracking when stable; easy to integrate with physical output devices. |
| How does it feel? | Natural and futuristic — like interacting with an invisible interface. |

**Video Demo:**  
https://drive.google.com/file/d/11zAG8wEilezNKS5cS4qRo5x8ATkNMcsk/view?usp=sharing 
---

## Summary 

By experimenting with different sensing libraries, I developed an understanding of how computer vision tools differ in flexibility, robustness, and responsiveness.  
My prototype — the **Air Dimmer** — demonstrates how real-time hand tracking can control a physical device, but also highlights challenges like lighting and stability.  

Next, I will refine and integrate the interaction into a final **observant system** and demonstrate it in use.

---

## Part 2 — Final Interactive System (coming next)
