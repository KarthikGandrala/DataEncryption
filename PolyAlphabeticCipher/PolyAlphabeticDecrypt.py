# Rotate function is intiated
def rotate(letter, key):
    # This series of statements encrypts any text that is in lowercase
    if letter.islower():
        
        # Decrypts the shift the user has inputted
        shift = ord(key) - ord('a')
        new = ord(letter) + -shift
        
        # Checks if new has gone past 'z'
        if new > ord('z'):
            new = new - 26
        
        # Checks if new has not gone past 'a'
        elif new < ord('a'):
            new = new + 26
        new = chr(new)
        
        # This series of statements encrypts anything in uppercase
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

# This series of statements decrypts the message
def decrypt(message, key):
    decrypted = ""
    counter = 0
    
    # Loop runs for the length of the users input message
    for i in range(len(message)):
        letter = message[i]
        
        # Encrypted Characters are concatenated 
        if letter.islower():
            subkey = key[counter % len(key)]
            decrypted = decrypted + rotate(letter, subkey)
            counter += 1
        else:
            decrypted = decrypted + letter
    return decrypted
