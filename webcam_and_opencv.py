import cv2

cap = cv2.VideoCapture(0)  # get image from webcam

# mog2_bgs = cv2.createBackgroundSubtractorMOG2()
# knn_bgs = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    cv2.imshow('Original', frame)

    # mog2_mask = mog2_bgs.apply(frame)
    # knn_mask = knn_bgs.apply(frame)

    edges = cv2.Canny(frame, 50, 100)
    cv2.imshow('edges', edges)

    # cv2.imshow('MOG2', mog2_mask)
    # cv2.imshow('KNN', knn_mask)

    k = cv2.waitKey(5) & 0xFF  # press ESC to quit
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
