import cv2
import os

image = cv2.imread("download.jpeg")  # Replace with the correct image path
secret_message = input("Enter secret message:")
passcode = input("Enter a passcode:")

encoding_dict = {}
decoding_dict = {}

for i in range(255):
    encoding_dict[chr(i)] = i
    decoding_dict[i] = chr(i)

row = 0
col = 0
channel = 0

for i in range(len(secret_message)):
    image[row, col, channel] = encoding_dict[secret_message[i]]
    row = row + 1
    col = col + 1
    channel = (channel + 1) % 3

cv2.imwrite("encryptedImage.jpg", image)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

decrypted_message = ""
row = 0
col = 0
channel = 0

passphrase = input("Enter passcode for Decryption")

if passcode == passphrase:
    for i in range(len(secret_message)):
        decrypted_message = decrypted_message + decoding_dict[image[row, col, channel]]
        row = row + 1
        col = col + 1
        channel = (channel + 1) % 3

    print("Decryption message:", decrypted_message)
else:
    print("Unauthorized Access")
