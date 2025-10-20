
# Ph-UI!!!

<details>
	<summary><strong>Instructions for Students (Click to Expand)</strong></summary>
  
	**Submission Cleanup Reminder:**
	- This README.md contains extra instructional text for guidance.
	- Before submitting, remove all instructional text and example prompts from this file.
	- You may delete these sections or use the toggle/hide feature in VS Code to collapse them for a cleaner look.
	- Your final submission should be neat, focused on your own work, and easy to read for grading.
  
	This helps ensure your README.md is clear, professional, and uniquely yours!
</details>

---

## Lab 4 Deliverables

### Part 1 (Week 1)
**Submit the following for Part 1:**  
*️⃣ **A. Capacitive Sensing**
	- Photos/videos of your Twizzler (or other object) capacitive sensor setup
		- <img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/f091165b-b8c0-4549-b90a-d4abf99d1b37" />
	- Code and terminal output showing touch detection
		- <img width="1386" height="620" alt="image" src="https://github.com/user-attachments/assets/44d8a8ce-966d-47be-b1a8-a6d915d8ef3b" />

*️⃣ **B. More Sensors**
	- Photos/videos of each sensor tested (light/proximity, rotary encoder, joystick, distance sensor)
		- <img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/0b4fb2ae-8f9f-4474-9b4f-668014e6a963" />
		- <img width="1402" height="788" alt="image" src="https://github.com/user-attachments/assets/c9fb52fa-0704-4a19-821c-04ff61727b86" />
		- <img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/24ef2ae9-6b41-4ed3-87e4-84918b322159" />
		- <img width="1400" height="624" alt="image" src="https://github.com/user-attachments/assets/6bf62e88-f993-4257-ae8e-c2ffa6a535fd" />
		- <img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/8e1dab78-8a93-49d4-a837-8b06c76c63c5" />
		- <img width="1478" height="792" alt="image" src="https://github.com/user-attachments/assets/4f378463-0975-4f91-a319-142b577794cd" />
		- <img width="858" height="880" alt="image" src="https://github.com/user-attachments/assets/d1c9b9a3-114e-470e-adf8-e5996a43bf6a" />
		- <img width="1508" height="664" alt="image" src="https://github.com/user-attachments/assets/8669f777-30e3-4f19-bc13-a0fdfb25e558" />
*️⃣ **C. Physical Sensing Design**
	- 5 sketches of different ways to use your chosen sensor
		- <img width="1200" height="1553" alt="image" src="https://github.com/user-attachments/assets/749df719-1d8a-4c57-9571-410b2c81e342" />
		- <img width="1200" height="1553" alt="image" src="https://github.com/user-attachments/assets/78cce206-2807-4e65-8a41-7a416db9529b" />
	- Written reflection: questions raised, what to prototype
	
	- Reflection: The sensors themselves seriously limit you on what kind of ideas you can use. 
	  While part 2 allows you to use one sensor, part 1 asks for you to come up with ideas from one sensor. 	  
	  In a sense it introduces a constraint and forces you to be creative, but it is also a little bit limiting. 
	
	- Questions:
		- Does the webcam count as it's own sensor? 
		- Woulnd't the buttons on the minifruit technically count as a twizzler? 
		  If yes, then can I use that as my sensor instead?
	
	- What to prototype:
		- Idea #2
	
	- Rationale for design		
		- It uses two sensors as part 2 requests and it uses machine learning techniques 
		  that I am very interested in. 

*️⃣ **D. Display & Housing**
	- 5 sketches for display/button/knob positioning
		- <img width="1200" height="1553" alt="image" src="https://github.com/user-attachments/assets/b9d763d4-0389-44cb-affa-1f75649d8794" />
		- <img width="1200" height="1553" alt="image" src="https://github.com/user-attachments/assets/0301bf74-662c-4687-a8c9-07c4c2a440ea" />
	- Written reflection: questions raised, what to prototype
	
	- Reflection: One thing that I noticed is that after the 2nd design for the housing, it became incrementally harder to come up with new designs. While I was still able to, 
	I felt like I had to take more time by the time I was at the 5th iteration. I also feel that the quality of the design started to taper off after the third design. 
	I think that's largely a result of my creativity running thin as I went from design to design.
	
	- Questions:
		- Can I use a material other than cardboard for housing?
		- Do I need some sort of cooling inside the housing?
		- Do i need to use a power source that allows you to move the housing wherever you want?(like a powerbank)
	
	- What to prototype:
		- Design #2
	
	- Rationale for design		
		- The most intuitive design out of all of them. I also find it to be the most ergonomic. 
	
	- Photos/videos of your cardboard prototype:		
<img width="1464" height="1042" alt="image" src="https://github.com/user-attachments/assets/ab0dd1fe-8747-4fe5-bb22-5f3b97f39184" />
<img width="1460" height="1006" alt="image" src="https://github.com/user-attachments/assets/8d57691c-ddfb-44d8-9f49-96e1fdc66033" />

---

### Part 2 (Week 2)
**Submit the following for Part 2:**  
*️⃣ **E. Multi-Device Demo**
	- Code and video for your multi-input multi-output demo (e.g., chaining Qwiic buttons, servo, GPIO expander, etc.)
	- Reflection on interaction effects and chaining

	Reflection: For some quick contenxt, I had first tried to implement the image classifier 
	and key input to add the object to the cart on my local machine. I used the rainforest api 
	to do a reverse lookup of the item that the YOLO classifier scanned and then I got that 
	object's ASIN number and added it to the link. However, this functionality is less practical 
	with a Raspberry Pi, as I'm running the script from the shell. Therefore, I switched to 
	using the Chromium browser and had the 'add to cart' process done via standard output. 
	I think that I was generally successful, but the YOLO classifier is not that accurate. 
	It also doesn't explicitly name products, so I most likely would need to implement a 
	classifier of my own. The following video shows a test of this. 
	Unfortunately, I could not get a video of me pressing the actual button. 
Video: [link](https://drive.google.com/file/d/11zAG8wEilezNKS5cS4qRo5x8ATkNMcsk/view?usp=sharing)


*️⃣ **F. Final Documentation**
	- Photos/videos of your final prototype
		- <img width="1168" height="972" alt="image" src="https://github.com/user-attachments/assets/2971c3bf-de78-442f-a292-723fec9400ce" />
	- Written summary: what it looks like, works like, acts like

	The design is the same as #2 in the housing sketches, as I felt that was the most 
	practical. I have the camera facing the front while the user presses the '0' tile 
	on the twizzler. Unlike the first implementation, this one does not open the browser
	and show you that the item has been added to your cart and instead does it via shell. 
	As mentioned prior, I use the chromium browser to do this, as I can't use headless 
	selenium with Chrome or Firefox. When an item is detected and the '0' tile on the 
	twizzler is pressed, then it gets added to the cart. The device acts similar to a 
	camera, but unlike cameras, you can directly capture object names from the video. 
	
	Reflection on what you learned and next steps: 
	I learned that it's singnificantly more difficult to write GET requests for the Pi
	due to me not using the GUI. I could have used it, but I felt that it took away from 
	the idea of designing a portable device. Overall, I think the product acted the way
	I intended for it to, but there were a few things that were unplanned such as the 
	specificity of the YOLO classifier and the introduction of a power bank as a power
	supply to truly make it portable. Going forward, I would wnat to train my own 
	classifier so that I can identify specific products rather than just objects. 
	

---

