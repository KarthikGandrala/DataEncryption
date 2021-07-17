#!/usr/bin/python
# -*- coding: utf-8 -*-


def encrypt(msg, key):
    encrypt_hex = ''
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])

        # zfill will pad a single letter hex with 0, to make it two letter pair

        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):

            # once all of the key's letters are used, repeat the key

            key_itr = 0
    return encrypt_hex


def decrypt(msg, key):

    hex_to_uni = ''
    for i in range(0, len(msg), 2):
        hex_to_uni += bytes.fromhex(msg[i:i + 2]).decode('utf-8')

    decryp_text = ''
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])

        # zfill will pad a single letter hex with 0, to make it two letter pair

        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):

            # once all of the key's letters are used, repeat the key

            key_itr = 0
    return decryp_text
