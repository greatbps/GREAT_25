# utils.py의 KoreaInvestEnv 클래스 수정

class KoreaInvestEnv:
    """한국투자증권 환경 설정 관리 클래스"""
    
    def __init__(self, config: dict[str, any]):
        """
        Args:
            config: 설정 딕셔너리
        """
        self.config = config
        self._setup_logging()

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

    def get_base_headers(self) -> dict[str, str]:
        """기본 HTTP 헤더 반환"""
        return {
            "content-type": "application/json",
            "appkey": self.config['api']['auth']['app_key'],
            "appsecret": self.config['api']['auth']['app_secret']
        }

    def get_full_config(self) -> dict[str, any]:
        """전체 설정 반환"""
        return self.config