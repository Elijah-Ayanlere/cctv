import cv2
from onvif import ONVIFCamera
import requests

# Camera Parameters
camera_url = "http://your_camera_ip:your_camera_port/stream"
username = "your_username"
password = "your_password"

# OpenCV VideoCapture with Authentication
capture = cv2.VideoCapture(camera_url)
capture.set(cv2.CAP_PROP_USERNAME, username)
capture.set(cv2.CAP_PROP_PASSWORD, password)

# Video Streaming Loop
while True:
    ret, frame = capture.read()
    if not ret:
        break
    
    # Process or display the captured frame as needed
    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera capture object
capture.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

# ONVIF Camera Parameters
cam_ip = "camera_ip"
cam_port = 80
cam_username = "username"
cam_password = "password"

# Create ONVIFCamera object
camera = ONVIFCamera(cam_ip, cam_port, cam_username, cam_password)

# Get Stream URI
media_service = camera.create_media_service()
profiles = media_service.GetProfiles()
profile_token = profiles[0].token  # Get the token of the first profile
stream_uri = media_service.GetStreamUri(
    StreamSetup={'Stream': 'RTP-Unicast', 'Transport': 'UDP'},
    ProfileToken=profile_token  # Pass the profile token
)
print("Stream URI:", stream_uri.Uri)

# Camera Login with Requests
login_url = "http://camera_ip/login"
username = "your_username"
password = "your_password"

# Form data for the login request
data = {
    "username": username,
    "password": password,
}

# Send a POST request to the login page
response = requests.post(login_url, data=data)

# Check the login response
if response.status_code == 200:
    print("Login successful")
    # You can perform additional actions after successful login
else:
    print("Login failed")



# CCTV Viewer using OpenCV and ONVIF

# This project demonstrates how to view a CCTV camera feed using Python, OpenCV, and the ONVIF protocol. The code includes two methods for accessing the camera: one using OpenCV with authentication and another using the ONVIFCamera library.

# Requirements

# - Python 3.x
# - OpenCV (`pip install opencv-python`)
# - ONVIF (`pip install onvif-zeep`)
# - Requests (`pip install requests`)

# Usage

# OpenCV VideoCapture with Authentication

# 1. Provide the camera URL, username, and password in the `camera_url`, `username`, and `password` variables.
# 2. Run the script using Python: `python opencv_cctv_viewer.py`.
# 3. The script will display the camera feed using OpenCV. Press 'q' to exit.

# ONVIF Camera with Stream URI and Login

# 1. Provide the camera IP, port, username, and password in the `cam_ip`, `cam_port`, `cam_username`, and `cam_password` variables.
# 2. Run the script using Python: `python onvif_cctv_viewer.py`.
# 3. The script will print the stream URI obtained using ONVIF. It will also attempt to log in to the camera using a POST request. Check the console for login success or failure.

# Note

# - Ensure that your CCTV camera supports the specified methods and protocols.
# - Update the camera URLs, credentials, and parameters according to your camera's specifications.

# Feel free to modify and extend the code for your specific use case.

# For any issues or questions, please refer to the documentation of the used libraries or seek assistance from the community.

