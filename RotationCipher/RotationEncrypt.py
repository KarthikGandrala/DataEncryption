def BasicRotate(letter, key):
    if letter.islower():
        new = ord(letter) + key
        if new > ord('z'):
            new = new - 26
        new = chr(new)
    else:
        new = letter
        
        if letter.isupper():
            new = ord(letter) + key
            if new > ord('Z'):
                new = new - 26
            new = chr(new)
        else:
            new = letter
    return new

def encryptBasicRotate(message, key):
    encrypted = ''
    for character in message:
        encrypted = encrypted + BasicRotate(character, key)
    return encrypted

# def runEncryptRotate(message, key):
#     print('Encrypted Value is: ' + encryptBasicRotate(message, key))

# runEncryptRotate()