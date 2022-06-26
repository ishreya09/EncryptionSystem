import ctypes

e = ctypes.CDLL("/home/ubuntu/Desktop/encrypt/EncryptionSystem/encrypt.so")

global key, text, address, shift,address_new

def encrypt_string():# strings
    e.encrypt_python_string(text.encode(),key.encode(),address_new.encode(),shift)


def decrypt_string():
    e.decrypt_python_string(text.encode(),key.encode(),address_new.encode(),shift)

def encrypt_file():
    e.encrypt_python_file(text.encode(),key.encode(),address.encode(),address_new.encode(),shift)    

def decrypt_file():
    e.decrypt_python_file(text.encode(),key.encode(),address.encode(),address_new.encode(),shift)    