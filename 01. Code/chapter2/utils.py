# utils.py
from Crypto.Cipher import AES 
from Crypto.Util.Padding import unpad
from base64 import b64encode
import pandas as pd

class KoreaInvestEnv:
    def __init__(self, cfg):
        self.custtype = cfg('custtype')
        
