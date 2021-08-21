#!/usr/bin/python
# -*- coding: utf-8 -*-

# The rotate function is defined


def rotate(letter, key):

    # Checks if letter is in lowercsae

    if letter.islower():

    #   Shifting of each character is carried out

        shift = ord(key) - ord('a')
        new = ord(letter) + shift

    # Checks if the letter has gone past z

        if new > ord('z'):
            new = new - 26
            
    # Checks if letter has not gone past a 
    
        elif new < ord('a'):

            new = new + 26
        new = chr(new)
    else:

    # If everything is fine, the program continues without subtracting or adding 26 to compensate

        new = letter

    # This algorithm executes if letter in uppercase
    
        if letter.isupper():
            new = ord(letter) + key
            
            # Checks if new has gone past capital Z
            
            if new > ord('Z'):
                new = new - 26
            new = chr(new)
            
        # Condition executes if none of these have been met
        
        else:
            new = letter
    return new


encrypted = ''
counter = 0


# Runs until i is not in the range of len(plaintext)

def polyPrint(message, key):
    encrypted = ''
    counter = 0
    spec = "~!@#$%^&*()_+}}][|::;><?/"
    for char in message:
        if str(char).isdigit() == True or spec.count(char) > 0:
            encrypted = "ERROR. Please input message with no integers or special characters"
            return encrypted
    
    for char in key:
        if str(char).isdigit() == True or spec.count(char) > 0:
            encrypted = "ERROR. Please input key with no integers or special characters"
            return encrypted
    # For loop written to split the message
    
    for i in range(len(message)):
        letter = message[i]

        # Checks if letter is lowercase
        
        if letter.islower():
            
            # Modulus operator used to check if remainder is there
            
            subkey = key[counter % len(key)]
            
            # Encrypted is assigned the rotated letter
            
            encrypted = encrypted + rotate(letter, subkey)
            counter += 1
        else:
            encrypted = encrypted + letter
            
    # In this end, encrypted is returned with all the encrypted letters
    
    return encrypted


