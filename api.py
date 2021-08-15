import re
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

sys.path.append("./lib")
from flask import Flask,request,jsonify,Response,render_template
app = Flask(__name__,
            static_url_path='', 
            static_folder='web',
            template_folder='web')
@app.route('/')
def index():
    return app.send_static_file('/index.html')

@app.route('/basicEncrypt', methods=['POST'])
def encryptData():
    print('received Post')
    
    # Get JSON data
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = int(record['key'])
    record = RotationEncrypt.encryptBasicRotate(m, k)
    recordInDict = {
        "data":record,
        "key":k
    }
    result = "Encrypted message with key is " + str(json.dumps(recordInDict["data"]))
    return result

@app.route('/basicDecrypt', methods=['POST'])
def decryptData():
    print('received Post')
    
    # Get JSON data
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = int(record['key'])
    record = RotationDecrypt.decrypt(m, k)
    recordInDict = {
        "data":record,
        "key":k
    }
    result = "The Encrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

@app.route('/polyEncrypt', methods=['POST'])
def polyData():
    print('received Post')
    
    # Get JSON data
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = str(record['key'])
    record = PolyAlphabeticEncrypt.polyPrint(m, k)
    recordInDict = {
        "data":record,
        "key":k
    }
    result = str(json.dumps(recordInDict["data"]))
    return result

@app.route('/polyDecrypt', methods=['POST'])
def polyData2():
    print('received Post')
    
    # Get JSON data
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = str(record['key'])
    record = PolyAlphabeticDecrypt.decrypt(m, k)
    recordInDict = {
        "data":record,
        "key":k
    }
    result = "The Decrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

@app.route('/xorEncrypt', methods=['POST'])
def xorData1():
    print('received Post')
    
    # Get JSON data
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = str(record['key'])
    record = XOREncrypt.encrypt(m, k)
    recordInDict = {
        "data":record,
        "key":k
    }
    result = "The Encrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

@app.route('/xorDecrypt', methods=['POST'])
def xorData2():
    print('received Post')
    
    # Get JSON data
    record = request.get_json()
    print(record)
    
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = str(record['key'])
    record = XOREncrypt.decrypt(m, k)
    recordInDict = {
        "data":record,
        "key":k
    }
    result = "The Decrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

@app.route('/cE', methods=['POST'])
def cus1():
    print('received Post')
    # Get JSON data
    record = request.get_json()
    print(record)
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = len(str(record['data']))
    record = CustomEncryptDecrypt.cipher_encryption(m, k)
    recordInDict = {
        "data":record,
        "key": k
    }
    result = "The Encrypted message is " + str(json.dumps(recordInDict["data"]))
    return result

@app.route('/cD', methods=['POST'])
def cus2():
    print('received Post')
    # Get JSON data
    record = request.get_json()
    print(record)
    # get_json() gives the data in the dict format
    m = str(record['data'])
    k = len(str(record['data']))
    record = CustomEncryptDecrypt.cipher_decryption(m, k)
    recordInDict = {
        "data":record,
        "key": k
    }
    result = "The Encrypted message is " + str(json.dumps(recordInDict["data"]))
    return result
app.run()




