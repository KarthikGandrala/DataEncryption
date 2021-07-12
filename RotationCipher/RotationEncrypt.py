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
    if key < 0 or key > 26:
        error = "ERROR. Out of range. Key Must be between 0 and 26"
        return error
    else:
        for character in message:
            encrypted = encrypted + BasicRotate(character, key)
            
    return encrypted, key
    

# def runEncryptRotate(message, key):
#     print('Encrypted Value is: ' + encryptBasicRotate(message, key))

# runEncryptRotate()