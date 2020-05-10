import cv2

cap = cv2.VideoCapture(0)  # get image from webcam

while True:
    ret, frame = cap.read()
    cv2.imshow('Original', frame)

    edges = cv2.Canny(frame, 50, 100)

    cv2.imshow('Edges', edges)

    k = cv2.waitKey(5) & 0xFF  # press ESC to quit
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
