# utils.py

import os
import yaml
import logging
from typing import Dict, Optional
import requests
from datetime import datetime, timedelta

class KoreaInvestEnv:
    """한국투자증권 환경 설정 관리 클래스"""
    
    def __init__(self, config_path: str = "config.yml"):
        self.config_path = config_path
        self.config = self._load_config()
        self._setup_logging()

    def _load_config(self) -> Dict:
        """설정 파일 로드"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"설정 파일 형식이 잘못되었습니다: {str(e)}")

    def _setup_logging(self):
        """로깅 설정"""
        logging.basicConfig(
            level=self.config['logging']['level'],
            format=self.config['logging']['format'],
            handlers=[
                logging.FileHandler(self.config['logging']['file']),
                logging.StreamHandler()
            ]
        )

    def get_api_config(self) -> Dict:
        """API 설정 반환"""
        return self.config['api']

class KoreaInvestAPI:
    """한국투자증권 API 클래스"""
    
    def __init__(self, env: KoreaInvestEnv):
        self.env = env
        self.api_config = env.get_api_config()
        self.access_token = None
        self.token_expires_at = None
        self.logger = logging.getLogger(__name__)

    def _get_access_token(self) -> str:
        """액세스 토큰 발급"""
        try:
            url = f"{self.api_config['base_url']}/oauth2/tokenP"
            headers = {
                "content-type": "application/json"
            }
            data = {
                "grant_type": "client_credentials",
                "appkey": self.api_config['auth']['app_key'],
                "appsecret": self.api_config['auth']['app_secret']
            }
            
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            
            token_data = response.json()
            self.access_token = token_data['access_token']
            self.token_expires_at = datetime.now() + timedelta(
                minutes=self.api_config['token']['access_token_expire_mins']
            )
            return self.access_token
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"토큰 발급 실패: {str(e)}")
            raise

    def get_token(self) -> str:
        """유효한 액세스 토큰 반환"""
        if (not self.access_token or 
            not self.token_expires_at or 
            datetime.now() >= self.token_expires_at):
            return self._get_access_token()
        return self.access_token

    def request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """API 요청 수행"""
        try:
            url = f"{self.api_config['base_url']}{endpoint}"
            headers = kwargs.pop('headers', {})
            headers['Authorization'] = f"Bearer {self.get_token()}"
            headers['appkey'] = self.api_config['auth']['app_key']
            headers['appsecret'] = self.api_config['auth']['app_secret']
            
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API 요청 실패: {str(e)}")
            raise