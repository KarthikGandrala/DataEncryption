#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function to encrypt message using key is defined

def encrypt(msg, key):
    
    # Defining empty strings and counters
    
    hexadecimal = ''
    iteration = 0
    
    # Running for loop in the range of MSG and comparing the BITS
    
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[iteration])

        # zfill will pad a single letter hex with 0, to make it two letter pair

        hexadecimal += hex(temp)[2:].zfill(2)
        
        
        # Checking if the iterations of the key are 1
        
        iteration += 1
        if iteration >= len(key):

            # once all of the key's letters are used, repeat the key

            iteration = 0
            
            # Returning the final value
            
    return hexadecimal


def decrypt(msg, key):

    # Defining hex to uni string to store

    hex_to_uni = ''
    
    # Running for loop to the length of message
    
    for i in range(0, len(msg), 2):
        
        # Decoding each individual bytes from hex
        
        hex_to_uni += bytes.fromhex(msg[i:i + 2]).decode('utf-8')

    decryp_text = ''
    iteration = 0
    
    # For loop running for the length of the hex to unicode string
    
    for i in range(len(hex_to_uni)):
        
        # Comparing each individual bit
        
        temp = ord(hex_to_uni[i]) ^ ord(key[iteration])

        # zfill will pad a single letter hex with 0, to make it two letter pair

        decryp_text += chr(temp)
        iteration += 1
        if iteration >= len(key):

            # once all of the key's letters are used, repeat the key

            iteration = 0
            
            # FInally return the decrypted text string
            
    return decryp_text
