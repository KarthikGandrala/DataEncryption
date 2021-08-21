#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def cipher_encryption(message, key):
    
    # For Loop runs to check if any special characters have been used
    
    spec = "~!@#$%^&*()_+}}][|::;><?/"
    
    # Loop runs through the users message
    
    for char in message:
        
        if spec.count(char) > 0:
            
            # If the message has characters in spec string, ERROR is returned
            
            encrypted = "ERROR. Please input message with no integers or special characters"
            return encrypted
    
    rot5 = '5678901234'

    # rot5 is being hardcoded here

    zeroToNine = '0123456789'
    rot_13_key = 13

    # rot 13 key is being defined here

    # loop runs in range of the message

    encryp_text = ''
    
    # Loop runs for suration of length of key
    
    for i in range(int(key)):
        
        temp = message[i] + ''
        
        # Temp stores message and the spce
        
        if ord(message[i]) == 32:
            
            # Checks bit count
            
            encryp_text += ' '
        elif re.search('[\d\s]+', temp):

        # rot5 key is being applied here
            # ROT5

            for j in range(len(zeroToNine)):
                
                # Numeric values will be encryped here
                
                if message[i] == zeroToNine[j]:
                    
                    # Assiging message i to new variable
                    
                    encryp_text += rot5[j]
        elif re.search('[\w\s]+', temp):

            # inner for

        # If its an integer, rot13 key is applied
            # ROT13

            ch_temp = ord(message[i]) + rot_13_key
            
            if ord(message[i]) == 32:
                
                encryp_text += ' '
                
            elif ch_temp > 90:

            # Checks if ch_temp is past 90

                ch_temp -= 26
                
                encryp_text += chr(ch_temp)
                
            else:
                
                encryp_text += chr(ch_temp)

    return encryp_text


def cipher_decryption(message, key):
    
    
    # Loop to check is any invalid characters in message
    
    spec = "~!@#$%^&*()_+}}][|::;><?/"
    
    for char in message:
        
        if spec.count(char) > 0:
            
            encrypted = "ERROR. Please input message with no integers or special characters"
            
            return encrypted

    # rot5 is harcoded here

    rot5 = '5678901234'
    
    zeroToNine = '0123456789'

    # rot13 is hardcoded here

    rot_13_key = 13

    decryp_text = ''

    # Loop runs until length of message

    for i in range(int(key)):
        
        # Loop runs for range of harcoded key
        
        temp = message[i] + ''
        
        # Space is added to temp
        
        if ord(message[i]) == 32:
            
            decryp_text += ' '
            
        elif re.search('[\d\s]+', temp):

        # Checks i alphanumeric
            # ROT5

            for j in range(len(zeroToNine)):
                
                if message[i] == rot5[j]:
                    
                    decryp_text += zeroToNine[j]
                    
        elif re.search('[\w\s]+', temp):

                    # inner for

        # Checks if integer
            # ROT13

            ch_temp = ord(message[i]) - rot_13_key
            
            if ord(message[i]) == 32:
                
                decryp_text += ' '
                
            elif ch_temp < 65:
                
                ch_temp += 26
                
                decryp_text += chr(ch_temp)
                
            else:
                
                decryp_text += chr(ch_temp)

    return decryp_text
