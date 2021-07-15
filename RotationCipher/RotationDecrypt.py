#!/usr/bin/python
# -*- coding: utf-8 -*-


def reverseBasicRotate(letter, key):
    if letter.islower():
        new = ord(letter) + key
        if new > ord('z'):
            new = new - 26
        if new < ord('a'):
            new = new + 26
        new = chr(new)
    else:
        new = letter

        if letter.isupper():
            new = ord(letter) + key
            if new > ord('Z'):
                new = new - 26
            if new < ord('A'):
                new = new + 26
            new = chr(new)
        else:
            new = letter

    return new


def encrypt(message, key):
    encrypted = ''
    for character in message:
        encrypted += reverseBasicRotate(character, key)
    return encrypted


def decrypt(message, key):
    return encrypt(message, -key)


# def runDecryptRotate(message, key):
#     print('Encrypted Value is: ' + decrypt(message, key))

# runDecryptRotate()
