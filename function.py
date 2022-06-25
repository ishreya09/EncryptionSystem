import ctypes

e = ctypes.CDLL("/home/ubuntu/Desktop/encrypt/EncryptionSystem/encrypt.so")

global key, text, address, shift

def encrypt():# strings
    e.text_init(text)

# decrypt - strings 
# 