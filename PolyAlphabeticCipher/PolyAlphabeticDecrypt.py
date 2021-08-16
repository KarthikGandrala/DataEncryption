#!/usr/bin/python
# -*- coding: utf-8 -*-
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
        elif new < ord('a'):

        # Checks if new has not gone past 'a'

            new = new + 26
        new = chr(new)
    else:

        # This series of statements encrypts anything in uppercase

        new = letter

        # Checks if letter is uppercase
        
        if letter.isupper():
            new = ord(letter) + key
            
            # Checks if letter has gone past capital Z
            
            if new > ord('Z'):
                
            # If new has gone past Z, 26 is then subtracted to balance it out
            
                new = new - 26
            new = chr(new)

        
        # If none of these situation are satisfied, new is appended
        else:
            new = letter
    return new


# This series of statements decrypts the message

def decrypt(message, key):
    
    # Empty string for appending and counter is defined
    
    decrypted = ''
    counter = 0
    spec = "~!@#$%^&*()_+}}][|::;><?/"
    for char in key:
        if str(char).isdigit() == True or spec.count(char) > 0:
            encrypted = "ERROR. Please input key with no integers or special characters"
            return encrypted

    # Loop runs for the length of the users input message

    for i in range(len(message)):
        letter = message[i]

        # If loop runs as long as letter is in lowercase

        if letter.islower():
            
            # Modulus operator is utilised to check if any remainder is present
            
            subkey = key[counter % len(key)]
            
            # result is appended to the decrypted string which stores the data
            
            decrypted = decrypted + rotate(letter, subkey)
            counter += 1
        else:
            decrypted = decrypted + letter
            
    # After the whole process has been completed for the length of string, decrypted is returned
    
    return decrypted
