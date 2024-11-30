import cv2
import numpy as np

# Включаем первую камеру
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
z = np.zeros((3,), dtype=np.uint8)
# Отключаем камеру
cap.release()
print(type(frame), frame)
print(len(frame), len(frame[0]), len(frame[0][0]))
for line in frame:
    for pixel in line:
        pixel = np.append(pixel, z[0])
        print(pixel, bytes(pixel))