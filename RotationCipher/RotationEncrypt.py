#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function to rotate each letter with the specified key

def BasicRotate(letter, key):
    
    # Checks if letter is lowercase
    
    if letter.islower():
        
        # As long as letter is lowercase, key is added
        
        new = ord(letter) + key
        
        # If letter has gone past z, 26 is subtracted to even it out
        
        if new > ord('z'):
            new = new - 26
        new = chr(new)
    else:
        
        # Else condition is defined to encrypt Upper case letters
        
        new = letter

        # Checks If letter is upper case, than key is added

        if letter.isupper():
            new = ord(letter) + key
            
            # If letter has gone past capital Z, 26 is subtracted to even it out
            
            if new > ord('Z'):
                new = new - 26
            new = chr(new)
            
        # If none of these conditions are satsifed, the letter is returned as is
            
        else:
            new = letter
    return new


def encryptBasicRotate(message, key):
    
    # Empty list defined to store the encrypted values
    
    encrypted = ''
    
    spec = "~!@#$%^&*()_+}}][|::;><?/"
    
    for char in message:
        
        if str(char).isdigit() == True or spec.count(char) > 0:
            
            encrypted = "ERROR. Please input message with no integers or special characters"
            
            return encrypted
    
    # Makes sure the key is within a valid range.
    
    if key < 0 or key > 26:
        
        # Error message returned if key is invalid
        
        error = 'ERROR. Out of range. Key Must be between 0 and 26'
        return error
    else:
        
        # For loop is run to the length of the message.
        
        for character in message:
            
            # Finally, the letters are appended to each other.
            
            encrypted = encrypted + BasicRotate(character, key)

    # Encrypted string is returned

    return encrypted


