# Camera Security System

This project implements a camera security system using Python and OpenCV. It detects motion in a video feed from the camera and triggers an alarm when motion is detected. Additionally, it sends a notification via a Telegram bot with an image of the detected motion.

## Features
- Real-time motion detection
- Telegram notification with motion image
- Adjustable motion threshold

## Prerequisites
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Telebot (`pip install pyTelegramBotAPI`)

## Usage
1. Clone this repository.
2. Replace the Telegram bot token and chat ID in the code with your own credentials.
3. Run the `camera_security_system.py` script.

## Configuration
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `TELEGRAM_CHAT_ID`: The chat ID where notifications will be sent.
- `roi`: Define the Region of Interest (ROI) for motion detection.

## How It Works
1. Captures video from the camera.
2. Computes the absolute difference between consecutive frames.
3. Applies a blur to reduce noise.
4. Thresholds the blurred difference.
5. Finds contours in the thresholded image.
6. Checks if motion exceeds the defined threshold.
7. Sends a notification if motion is detected.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
