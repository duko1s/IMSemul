import cv2
import numpy as np
z = np.zeros((3,), dtype=np.uint8)

# Включаем первую камеру
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    print("get frame from web camera is ok!")
else:
    quit()
# Отключаем камеру
cap.release()
# Что такое фрейм
# print(type(frame), frame)
print(len(frame), len(frame[0]), len(frame[0][0]))
count_pixels = len(frame) * len(frame[0])
# сохраняем фрейм как битмап файл и пробуем просмотреть стандартными средствами ОС
with open("test.bmp","w+b") as f:
    print("create header of bmp file....")
    # BITMAPFILEHEADER
    f.write(b'BM')#ID field (42h, 4Dh)
    f.write((count_pixels * 4 + 122).to_bytes(4,byteorder="little"))#154 bytes (122+32) Size of the BMP file
    f.write((0).to_bytes(2,byteorder="little"))#Unused
    f.write((0).to_bytes(2,byteorder="little"))#Unused
    f.write((122).to_bytes(4,byteorder="little"))#122 bytes (14+108) Offset where the pixel array (bitmap data) can be found
    # BITMAPINFO
    # версия 
    # BITMAPV4HEADER
    f.write((108).to_bytes(4,byteorder="little"))#108 bytes Number of bytes in the DIB header (from this point)
    f.write((len(frame[0])).to_bytes(4,byteorder="little"))#Width of the bitmap in pixels
    f.write((len(frame)).to_bytes(4,byteorder="little"))#Height of the bitmap in pixels
    f.write((1).to_bytes(2,byteorder="little"))#1 plane Number of color planes being used
    f.write((32).to_bytes(2,byteorder="little"))#32 bits Number of bits per pixel
    f.write((3).to_bytes(4,byteorder="little"))#3 BI_BITFIELDS, no pixel array compression used
    f.write((count_pixels * 4).to_bytes(4,byteorder="little"))#32 bytes Size of the raw bitmap data (including padding)
    f.write((2835).to_bytes(4,byteorder="little"))#2835 pixels/metre horizontal Print resolution of the image,
    f.write((2835).to_bytes(4,byteorder="little"))#2835 pixels/metre vertical   72 DPI × 39.3701 inches per metre yields 2834.6472
    f.write((0).to_bytes(4,byteorder="little"))#0 colors Number of colors in the palette
    f.write((0).to_bytes(4,byteorder="little"))#0 important colors 0 means all colors are important
    f.write(b'\x00\x00\xFF\x00')#00FF0000 in big-endian Red channel bit mask (valid because BI_BITFIELDS is specified)
    f.write(b'\x00\xFF\x00\x00')#0000FF00 in big-endian Green channel bit mask (valid because BI_BITFIELDS is specified)
    f.write(b'\xFF\x00\x00\x00')#000000FF in big-endian Blue channel bit mask (valid because BI_BITFIELDS is specified)
    f.write(b'\x00\x00\x00\xFF')#FF000000 in big-endian Alpha channel bit mask
    f.write(b' niW')#little-endian "Win " LCS_WINDOWS_COLOR_SPACE
    f.write((0).to_bytes(36,byteorder="little"))#CIEXYZTRIPLE Color Space endpoints	Unused for LCS "Win " or "sRGB"
    f.write((0).to_bytes(4,byteorder="little"))#0 Red Gamma Unused for LCS "Win " or "sRGB"
    f.write((0).to_bytes(4,byteorder="little"))#0 Green Gamma Unused for LCS "Win " or "sRGB"
    f.write((0).to_bytes(4,byteorder="little"))#0 Blue Gamma Unused for LCS "Win " or "sRGB"
    print("write pixels on bmp file....")
    for line in frame:
        for pixel in line:
            pixel = np.append(pixel, z[0])
            f.write(pixel)
    # f.write(b'\xFF\x00\x00\x7F')#255 0 0 127 Blue (Alpha: 127), Pixel (1,0)
    # f.write(b'\x00\xFF\x00\x7F')#0 255 0 127 Green (Alpha: 127), Pixel (1,1)
    # f.write(b'\x00\x00\xFF\x7F')#0 0 255 127 Red (Alpha: 127), Pixel (1,2)
    # f.write(b'\xFF\xFF\xFF\x7F')#255 255 255 127 White (Alpha: 127), Pixel (1,3)
    # f.write(b'\xFF\x00\x00\xFF')#255 0 0 255 Blue (Alpha: 255), Pixel (0,0)
    # f.write(b'\x00\xFF\x00\xFF')#0 255 0 255 Green (Alpha: 255), Pixel (0,1)
    # f.write(b'\x00\x00\xFF\xFF')#0 0 255 255 Red (Alpha: 255), Pixel (0,2)
    # f.write(b'\xFF\xFF\xFF\xFF')#255 255 255 255 White (Alpha: 255), Pixel (0,3)
    f.close()
    print("succefull done! open test.bmp file on standart viewer....")