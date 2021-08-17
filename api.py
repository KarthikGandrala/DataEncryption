# Importing all required standard modules and functions from custom modules

import sys
import json
import RotationCipher
from RotationCipher import RotationEncrypt,RotationDecrypt
import PolyAlphabeticCipher
from PolyAlphabeticCipher import PolyAlphabeticEncrypt,PolyAlphabeticDecrypt
import XORCipher
from XORCipher import XOREncrypt
import CustomAlgorithm
from CustomAlgorithm import CustomEncryptDecrypt
import re

# Importing Flask and required functions from Flask

sys.path.append("./lib")
from flask import Flask,request,jsonify,Response,render_template

# Defining the path of the files

app = Flask(__name__,
            static_url_path='', 
            static_folder='web',
            template_folder='web')

# Route specified in order to gather information

@app.route('/')
def index():
    return app.send_static_file('/index.html')

# Defining what I wanted to do with the data, in this case POST

@app.route('/basicEncrypt', methods=['POST'])

# Function defined to gather input and apply algorithms

def encryptData():
    
    # This is printed to the python console to confirm that the POST has been received
    
    print('received Post')
    
    # JSON data is gathered for conversion
    
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    
    m = str(record['data'])
    k = int(record['key'])
    
    # Encryption/DEcryption function is applied to the data
    
    record = RotationEncrypt.encryptBasicRotate(m, k)
    
    # Encrypted/Decrypted data is assigned to a short data dictionary
    
    recordInDict = {
        "data":record,
        "key":k
    }
    
    # Data is appended to result and is finally returned
    
    result = "Encrypted message with key is " + str(json.dumps(recordInDict["data"]))
    return result

# Function defined to gather input and apply algorithms

@app.route('/basicDecrypt', methods=['POST'])
def decryptData():
    
    # This is printed to the python console to confirm that the POST has been received
    
    print('received Post')
    
   # JSON data is gathered for conversion
    
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = int(record['key'])
    
    # Encryption/DEcryption function is applied to the data

    record = RotationDecrypt.decrypt(m, k)
    
    # Encrypted/Decrypted data is assigned to a short data dictionary

    recordInDict = {
        "data":record,
        "key":k
    }
    
    # Data is appended to result and is finally returned

    result = "The Decrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

# Function defined to gather input and apply algorithms

@app.route('/polyEncrypt', methods=['POST'])
def polyData():
    
    # This is printed to the python console to confirm that the POST has been received

    print('received Post')
    
   # JSON data is gathered for conversion
   
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = str(record['key'])
    
    # Encryption/DEcryption function is applied to the data

    record = PolyAlphabeticEncrypt.polyPrint(m, k)
    
    # Data is appended to result and is finally returned

    recordInDict = {
        "data":record,
        "key":k
    }
    
    # Data is appended to result and finally returned
    
    result = str(json.dumps(recordInDict["data"]))
    return result


# Function to encrypt/decrypt has been defined

@app.route('/polyDecrypt', methods=['POST'])
def polyData2():
    print('received Post')
    
    # JSON data is gathered for encryption/decryption
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    
    m = str(record['data'])
    k = str(record['key'])
    
    # Encryption/DEcryption function is applied to the data

    record = PolyAlphabeticDecrypt.decrypt(m, k)
    
    # Encrypted/Decrypted data is assigned to a short data dictionary

    recordInDict = {
        "data":record,
        "key":k
    }
    
    # Data is appended to result and is finally returned

    result = str(json.dumps(recordInDict["data"]))
    return result

# Function is defined for encryption/decryption

@app.route('/xorEncrypt', methods=['POST'])
def xorData1():
    print('received Post')
    
    # JSON data input is gathered for encryption/decryptiom
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = str(record['key'])
    
    # Encryption/Decryption functions is applied to the data
    
    record = XOREncrypt.encrypt(m, k)
    
    # Data is added to a short data dictionary
    
    recordInDict = {
        "data":record,
        "key":k
    }
    
    # Data is added to result and returned for display 
    
    result = "The Encrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

# Function is defined for encryption/decryption

@app.route('/xorDecrypt', methods=['POST'])
def xorData2():
    print('received Post')
    
    # Get JSON data for encryption/decryption
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = str(record['key'])
    
    # Encryption/decryption functions are applied to the data
    
    record = XOREncrypt.decrypt(m, k)
    
    # Data is appended to a short dictionary
    
    recordInDict = {
        "data":record,
        "key":k
    }
    
    # Data is finally appended to result and returned for display
    
    result = "The Decrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

# Function is defined for encryption/decryption

@app.route('/cE', methods=['POST'])
def cus1():
    
    # Indicates POST has been recived
    
    print('received Post')
    
    
    # Get JSON data for encryption/decryption
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    
    m = str(record['data'])
    k = len(str(record['data']))
    
    # encryption/decryption function is applied to the data
    
    record = CustomEncryptDecrypt.cipher_encryption(m, k)
    
    # data is added to a short data dictionary
    
    recordInDict = {
        "data":record,
        "key": k
    }
    
    # Encrypted/decrypted data ia added to result and returned
    
    result = "The Encrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

@app.route('/cD', methods=['POST'])

# Function defined for encryption/decryption

def cus2():
    
    # Confirms post has been recieved
    
    print('received Post')
    
    # Get JSON data for encryption/decryption
    
    record = request.get_json()
    print(record)
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = len(str(record['data']))
    
    # Encryption/decryption applied to the data
    
    record = CustomEncryptDecrypt.cipher_decryption(m, k)
    
    # Data appended to record and returned for display
    
    recordInDict = {
        "data":record,
        "key": k
    }
    
    # Final result is appended to result and returned to user
    
    result = "The decrypted message is " + str(json.dumps(recordInDict["data"]))
    return result
app.run()




