import requests
import json
import datetime
import time
import yaml


APP_KEY = "PSb6tRnToOep8OASOkZ9hfK5NHEiW3GQTMbk"
APP_SECRET = "HRpEQmVTUjX/cQki0XcyYrLngE6pTZJfYz+rXshlYP1+/CpV9tVi3bU6Rxz8pC0LLSaKehCqwB67UKnPAl9icWDUCGw8WO5Bb+CJODPcIZ9jo/1T9Km/Wq8Ri9RErkIbprWVCS5Zh0Vjbbv9Qt65A124rSB/rDb3mI0KxPB3qQHIgmzKbKg="
ACCESS_TOKEN = ""
CANO = "64556264"
ACNT_PRDT_CD = "01"
#DISCORD_WEBHOOK_URL = _cfg['DISCORD_WEBHOOK_URL']
URL_BASE = "https://openapi.koreainvestment.com:9443"

def get_access_token():
    """토큰 발급"""
    headers = {"content-type":"application/json"}
    body = {"grant_type":"client_credentials",
    "appkey":APP_KEY, 
    "appsecret":APP_SECRET}
    PATH = "oauth2/tokenP"
    URL = f"{URL_BASE}/{PATH}"
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    ACCESS_TOKEN = res.json()["access_token"]
    return ACCESS_TOKEN
    

def get_current_price(code="005930"):
    """현재가 조회"""
    PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
    URL = f"{URL_BASE}/{PATH}"
    headers = {"Content-Type":"application/json", 
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "appKey":APP_KEY,
            "appSecret":APP_SECRET,
            "tr_id":"FHKST01010100"}
    params = {
    "fid_cond_mrkt_div_code":"J",
    "fid_input_iscd":code,
    }
    res = requests.get(URL, headers=headers, params=params)
    return int(res.json()['output']['stck_prpr'])
# 자동매매 시작
try:
    ACCESS_TOKEN = get_access_token()

    symbol_list = ["005930","035720","000660","069500"] # 매수 희망 종목 리스트
    price = get_current_price("035720")
    print(price)
    
except Exception as e:
    
    time.sleep(1)