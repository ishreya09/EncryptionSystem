import ctypes

e = ctypes.CDLL("/home/ubuntu/Desktop/encrypt/EncryptionSystem/encrypt.so")

global key, text, address, shift,address_new

def encrypt_string():# strings
    e.text_init(text)
    e.key_init(key)
    e.shift_init(shift)
    e.makeMatrix()
    e.makeKeyword()
    e.encrypt()
    p= e.getText()
    return p


def decrypt_string():
    e.text_init(text)
    e.key_init(key)
    e.shift_init(shift)
    e.address_init(address)
    e.makeMatrix()
    e.makeKeyword()

    e.decrypt()
    c=e.getText()
    return c

def encrypt_file(filename):
    e.address_init(address)
    e.file_input()
    e.write_another_file(address_new)
    p= e.getText()

    return p

def decrypt_file(filename):
    e.address_init(address)
    e.file_input()
    e.write_another_file(address_new)
    p= e.getText()

    return p