import requests
import json
import datetime
import time
import yaml
from typing import List, Dict, Optional
import logging
import pandas as pd

class KoreaInvestmentAPI:
    def __init__(self, app_key: str, app_secret: str, account_number: str, product_code: str = "01"):
        """
        Initialize the Korea Investment API client
        
        Args:
            app_key: API application key
            app_secret: API application secret
            account_number: Trading account number
            product_code: Product code (default: "01" for stocks)
        """
        self.app_key = app_key
        self.app_secret = app_secret
        self.account_number = account_number
        self.product_code = product_code
        self.base_url = "https://openapi.koreainvestment.com:9443"
        self.access_token = None
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def get_access_token(self) -> str:
        """토큰 발급"""
        try:
            headers = {"content-type": "application/json"}
            body = {
                "grant_type": "client_credentials",
                "appkey": self.app_key,
                "appsecret": self.app_secret
            }
            
            response = requests.post(
                f"{self.base_url}/oauth2/tokenP",
                headers=headers,
                data=json.dumps(body)
            )
            response.raise_for_status()
            
            self.access_token = response.json()["access_token"]
            self.logger.info("Successfully obtained new access token")
            return self.access_token
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to get access token: {str(e)}")
            raise

    def get_minute_chart(self, stock_code: str, minutes: int = 1, count: int = 30) -> pd.DataFrame:
        """
        1분봉 데이터 조회
        
        Args:
            stock_code: 종목 코드 (예: "005930")
            minutes: 분봉 단위 (1, 3, 5, 10, 15, 30, 45, 60 중 선택)
            count: 조회할 데이터 개수 (최대 100)
            
        Returns:
            DataFrame: 분봉 데이터
        """
        try:
            if not self.access_token:
                self.get_access_token()

            headers = {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": f"Bearer {self.access_token}",
                "appKey": self.app_key,
                "appSecret": self.app_secret,
                "tr_id": "FHKST03010200"  # 주식 분봉 조회 TR ID
            }
            
            params = {
                "fid_etc_cls_code": "",
                "fid_cond_mrkt_div_code": "J",
                "fid_input_iscd": stock_code,
                "fid_input_hour_1": f"{minutes}",
                "fid_pw_data_incu_yn": "Y",
                "fid_req_cnt": f"{count}"
            }
            
            response = requests.get(
                f"{self.base_url}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice",
                headers=headers,
                params=params
            )
            response.raise_for_status()
            
            data = response.json()['output2']
            
            # DataFrame 변환
            df = pd.DataFrame(data)
            
            # 컬럼명 한글로 변경 및 데이터 타입 변환
            df = df.rename(columns={
                'stck_cntg_hour': '시간',
                'stck_prpr': '현재가',
                'stck_oprc': '시가',
                'stck_hgpr': '고가',
                'stck_lwpr': '저가',
                'cntg_vol': '거래량',
            })
            
            # 데이터 타입 변환
            numeric_columns = ['현재가', '시가', '고가', '저가', '거래량']
            df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
            
            # 시간 포맷 변경 (HHMMSS -> HH:MM:SS)
            df['시간'] = pd.to_datetime(df['시간'], format='%H%M%S').dt.strftime('%H:%M:%S')
            
            # 인덱스 재설정 (최신 데이터가 위로 오도록)
            df = df.sort_values('시간', ascending=False).reset_index(drop=True)
            
            self.logger.info(f"Successfully retrieved {minutes}-minute chart data for {stock_code}")
            return df
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to get minute chart for {stock_code}: {str(e)}")
            return None

def main():
    # 설정
    CONFIG = {
        "APP_KEY": "PSb6tRnToOep8OASOkZ9hfK5NHEiW3GQTMbk",  # 발급받은 APP KEY 입력
        "APP_SECRET": "HRpEQmVTUjX/cQki0XcyYrLngE6pTZJfYz+rXshlYP1+/CpV9tVi3bU6Rxz8pC0LLSaKehCqwB67UKnPAl9icWDUCGw8WO5Bb+CJODPcIZ9jo/1T9Km/Wq8Ri9RErkIbprWVCS5Zh0Vjbbv9Qt65A124rSB/rDb3mI0KxPB3qQHIgmzKbKg=",  # 발급받은 APP SECRET 입력
        "ACCOUNT_NUMBER": "64556264",
        "WATCH_LIST": [stno]  # 관심종목 리스트
    }
    
    try:
        # API 클라이언트 초기화
        client = KoreaInvestmentAPI(
            app_key=CONFIG["APP_KEY"],
            app_secret=CONFIG["APP_SECRET"],
            account_number=CONFIG["ACCOUNT_NUMBER"]
        )
        
        # 각 종목의 1분봉 데이터 조회
        for stock_code in CONFIG["WATCH_LIST"]:
            df = client.get_minute_chart(stock_code, minutes=1, count=100)
            if df is not None:
                print(f"\n종목코드: {stock_code} 1분봉 데이터")
                print(df)  # 최근 5개 데이터 출력
                
            time.sleep(1)  # API 호출 간격 조절
            
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다...")
    except Exception as e:
        logging.error(f"예상치 못한 오류 발생: {str(e)}")
        raise

if __name__ == "__main__":
    stno = "005930"
    main()