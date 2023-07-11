import cv2

# Create a VideoCapture object to capture video from the camera
ip = ''
"https://192.168.153.38:8080/video"

cap = cv2.VideoCapture(ip)  # 0 represents the default camera; you can change it to the desired camera index if multiple cameras are available

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    
    exit()

# Initialize variables for cropping
start_x, start_y, end_x, end_y = 0, 0, 0, 0
cropping = False

def mouse_callback(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        end_x, end_y = x, y
        cropping = False

# Create a window and set the mouse callback function
cv2.namedWindow("Camera Stream")
cv2.setMouseCallback("Camera Stream", mouse_callback)

while True:
    # Read the current frame from the stream
    ret, frame = cap.read()
    w,h,c = frame.shape
    frame = cv2.resize(frame,(h//2,w//2))
    # Display the frame
    cv2.imshow("Camera Stream", frame)

    # If cropping is enabled, show the cropping rectangle
    if cropping:
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

    # Wait for 'q' key to exit or 'c' key to perform the crop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c') and not cropping:
        cropped_image = frame[start_y:end_y, start_x:end_x]
        cv2.imshow("Cropped Image", cropped_image)
        cv2.imwrite("Maze.png", cropped_image)

        # cv2.waitKey(0)  # Wait until a key is pressed to close the cropped image window

# Release the VideoCapture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
import subprocess

# Command to execute in cmd
command = "python Main.py"  # Replace with your desired command

# Run the command
result = subprocess.run(command, shell=True, capture_output=True, text=True)