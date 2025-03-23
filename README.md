# QR Code Scanner

## Overview
This project is a simple QR code scanner using OpenCV and Pyzbar in Python. It captures video from the webcam, detects QR codes in real-time, and displays the decoded text on the screen while drawing a bounding box around the detected QR code.

## Requirements
Ensure you have the following dependencies installed before running the script:

```sh
pip install opencv-python numpy pyzbar
```

## How to Use
1. **Run the Script**: Execute the Python script to start the webcam and begin scanning for QR codes.

```sh
python qr_scanner.py
```

2. **Point a QR Code at the Camera**: The program will detect and decode the QR code in real-time.
3. **Read the Output**: The decoded text will be displayed on the screen and printed in the terminal.
4. **Exit**: Press `Esc` or close the window to stop the program.

## Code Breakdown
- **Capture Video**: Uses OpenCV to open the default webcam.
- **Detect QR Codes**: Uses Pyzbar to scan each frame for QR codes.
- **Draw Bounding Box**: Uses OpenCV to highlight the detected QR code.
- **Display Decoded Text**: Shows the text inside the frame and prints it to the console.

## Troubleshooting
- If the camera does not start, ensure it is properly connected and accessible.
- If QR codes are not being detected, try increasing the camera resolution or ensuring proper lighting.

## Future Enhancements
- Add support for multiple camera sources.
- Save scanned QR codes to a file for logging.
- Implement a graphical user interface (GUI) for improved usability.

## License
This project is open-source and available for modification and distribution.

