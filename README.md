# CCTV Viewer using OpenCV and ONVIF

This project provides a Python script for viewing CCTV camera feeds using the OpenCV library with authentication and the ONVIF protocol. The code includes two methods to access the camera stream, offering flexibility depending on the camera's capabilities.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- ONVIF (`pip install onvif-zeep`)
- Requests (`pip install requests`)

## Usage

### OpenCV VideoCapture with Authentication

1. **Configure the Camera Parameters:**
   - Replace `your_camera_ip`, `your_camera_port`, `your_username`, and `your_password` with your CCTV camera's details in the `camera_url`, `username`, and `password` variables.

2. **Run the Script:**
   - Execute the script using Python: `python opencv_cctv_viewer.py`.

3. **View the Camera Feed:**
   - The script will use OpenCV to display the live CCTV camera feed. Press 'q' to exit.

### ONVIF Camera with Stream URI and Login

1. **Configure the ONVIF Camera Parameters:**
   - Replace `camera_ip`, `cam_port`, `username`, and `password` with your CCTV camera's ONVIF details.

2. **Run the Script:**
   - Execute the script using Python: `python onvif_cctv_viewer.py`.

3. **View Stream URI and Attempt Login:**
   - The script will print the obtained stream URI using ONVIF. It will also attempt to log in to the camera using a POST request. Check the console for login success or failure.

## Note for CCTV Usage

- Ensure that your CCTV camera supports either the OpenCV method with authentication or the ONVIF protocol.
- Update the camera URLs, credentials, and parameters based on your CCTV camera's specifications.
- Regularly check and follow the security guidelines provided by the camera manufacturer.
- Customize the script to fit your specific use case or integrate it into a larger CCTV monitoring system.

Feel free to adapt and extend the code to suit your requirements.

For any issues or questions, refer to the documentation of the used libraries or seek assistance from the community.
