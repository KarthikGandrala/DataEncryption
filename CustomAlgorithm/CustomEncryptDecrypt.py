import re

def cipher_encryption(message):
    rot5 = "5678901234"
    zeroToNine = "0123456789"
    rot_13_key = 13
    encryp_text = "";
    for i in range(len(message)):
        temp = message[i] + ""
        if ord(message[i]) == 32:
            encryp_text += " "
        elif re.search('[\d\s]+', temp):
            # ROT5
            for j in range(len(zeroToNine)):
                if message[i] == zeroToNine[j]:
                    encryp_text += rot5[j]
            # inner for
        elif re.search('[\w\s]+', temp):
            # ROT13
            ch_temp = ord(message[i]) + rot_13_key
            if ord(message[i]) == 32:
                encryp_text += " "
            elif ch_temp > 90:
                ch_temp -= 26
                encryp_text += chr(ch_temp)
            else:
                encryp_text += chr(ch_temp)
        # if-else
    # for

    return encryp_text


def cipher_decryption(message):
    rot5 = "5678901234"
    zeroToNine = "0123456789"
    rot_13_key = 13
    
    decryp_text = "";
    for i in range(len(message)):
        temp = message[i] + ""
        if ord(message[i]) == 32:
            decryp_text += " "
        elif re.search('[\d\s]+', temp):
            # ROT5
            for j in range(len(zeroToNine)):
                if message[i] == rot5[j]:
                    decryp_text += zeroToNine[j]
                    # inner for
        elif re.search('[\w\s]+', temp):
            # ROT13
            ch_temp = ord(message[i]) - rot_13_key
            if ord(message[i]) == 32:
                decryp_text += " "
            elif ch_temp < 65:
                ch_temp += 26
                decryp_text += chr(ch_temp)
            else:
                decryp_text += chr(ch_temp)
                # if-else
    # for

    return decryp_text



