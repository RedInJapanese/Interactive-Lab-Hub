import cv2
from ultralytics import YOLO
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import time
import board
import busio
import adafruit_mpr121
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# Load the YOLOv8 model (you can use "yolov8n.pt" for speed or "yolov8m.pt" for accuracy)
model = YOLO("yolov8n.pt")

# Open the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")  # no GUI
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

# Use the correct chromedriver
service = Service("/usr/bin/chromedriver")

# Launch Chromium via Selenium
driver = webdriver.Chrome(service=service, options=options)


if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Press 'q' to quit")

animate = [
    "person", "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe"]


api_key = "1E638B734DA64F17B4AAD4DA6A717ADF"
search_term = "Echo Dot 5th Generation"

url = "https://api.rainforestapi.com/request"
# params = {
#     "api_key": api_key,
#     "type": "search",
#     "amazon_domain": "amazon.com",
#     "search_term": search_term
# }
item = ""
def add_cart(item):
    params = {
        "api_key": api_key,
        "type": "search",
        "amazon_domain": "amazon.com",
        "search_term": item
    }
    response = requests.get(url, params=params)
    data = response.json()


    # Extract ASINs from the search results
    for product in data.get("search_results", []):
        title = product.get("title")
        asin = product.get("asin")


    # Use Chrome so you can log in normally
    driver = webdriver.Chrome(service=service, options=options)
    # Open the product page
    driver.get("https://www.amazon.com/dp/" + str(data.get("search_results", [])[0].get("asin")))

    # Wait for page to load and log in manually if needed
    time.sleep(10)

    # Click "Add to Cart"
    add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
    add_to_cart.click()

    driver.quit()
    print("Item added to cart!")
def scan():
    while True:
        ret, frame = cap.read()
        if not ret:
            print(" Failed to grab frame")
            break

        # Run YOLO detection
        results = model(frame, stream=True)

        # Draw results on the frame
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                if model.names[cls] not in animate:
                    label = model.names[cls]
                    item = label
                    conf = box.conf[0]
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    print(f"FOUND ITEM {label}")
                    # # Draw bounding box and label
                    # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    # cv2.putText(frame, f"{label} ({conf:.2f})", (x1, y1 - 10),
                    #             cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        # Display the frame
        # cv2.imshow("YOLOv8 Live Detection", frame)
        key = cv2.waitKey(1) & 0xFF
        # Press 'q' to quit

        if mpr121[0].value:
            print("adding to cart")
            add_cart(item)
        time.sleep(0.25)  # Small delay to keep from spamming output messages.

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            return

scan()
cap.release()
cv2.destroyAllWindows()



cap.release()
cv2.destroyAllWindows()
