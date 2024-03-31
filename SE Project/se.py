import cv2
import telebot

# Initialize your Telegram bot token
TELEGRAM_BOT_TOKEN = '6743738517:AAGrbDFJrBkpRA7LmKqoU_hYLNy_aXAhxss'

TELEGRAM_CHAT_ID = '1867562203'

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Function to detect motion in the video feed
def detect_motion(frame1, frame2, roi):
    # Convert frames to grayscale
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Apply ROI
    roi_gray1 = gray1[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
    roi_gray2 = gray2[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]

    # Compute absolute difference between frames
    frame_diff = cv2.absdiff(roi_gray1, roi_gray2)

    # Apply a blur to the difference to reduce noise
    frame_diff_blurred = cv2.GaussianBlur(frame_diff, (5, 5), 0)

    # Threshold the blurred difference
    _, thresh = cv2.threshold(frame_diff_blurred, 20, 255, cv2.THRESH_BINARY)

    # Find contours of the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Define a motion threshold - adjust as needed
    motion_threshold = 1000

    # Check if contours is not empty and motion exceeds the threshold
    if contours and cv2.contourArea(contours[0]) > motion_threshold:
        return True
    else:
        return False

# Capture video from the camera
cap = cv2.VideoCapture(0)

# Read initial frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Define Region of Interest (ROI) [x, y, width, height]
roi = [100, 100, 400, 300]

while True:
    # Read current frame
    ret, current_frame = cap.read()

    # Check for motion
    if detect_motion(frame1, current_frame, roi):
        print("Motion detected! Triggering alarm.")

        # Save the image with detected motion
        cv2.imwrite("motion_detected.jpg", current_frame)

        # Send a notification via Telegram bot with the image
        photo = open("motion_detected.jpg", "rb")
        bot.send_photo(TELEGRAM_CHAT_ID, photo, caption="Motion detected! Triggering alarm.")
        photo.close()

    # Update frames for the next iteration
    frame1 = frame2
    frame2 = current_frame

    # Display the video feed
    cv2.imshow('Camera Motion Sensor', current_frame)

    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()