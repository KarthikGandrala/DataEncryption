
def xor(character, key):
    code = ord(character) ^ ord(key)
    result = chr(code)
    return result

def encrypt(message, key):
    encrypted = ''
    for character in message:
        encrypted = encrypted + xor(character, key)
    return encrypted

# print(encrypt("hello", "#"))